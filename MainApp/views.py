from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from .models import Tenant,Invoice
from .models import Profile
from .forms import InvoiceForm
from django.core.exceptions import ValidationError



# Create your views here.


def index(request):
    return render(request,"MainApp/index.html")


def edit_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST' and request.FILES.get('profile_photo'):
        profile.photo = request.FILES['profile_photo']  
        profile.save()
        messages.success(request, 'Profile photo updated successfully!')
        return redirect('index')  
    return render(request, 'MainApp/edit_profile.html', {'profile': profile})

@login_required(login_url='log_in')
def change_password(request):
    form=PasswordChangeForm(user=request.user)
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            name=form.save()
            update_session_auth_hash(request,name)
            messages.success(request,'Password changed successfully')
            return redirect('index')
    return render(request,'MainApp/change_password.html',{'form':form})



def view_profile(request):
    return render(request, 'MainApp/view_profile.html')


def rental(request):
    if request.method == 'POST':
        photo = request.FILES.get('tenant_photo')
        name = request.POST.get('tenant_name')
        address = request.POST.get('tenant_address')
        mobile = request.POST.get('tenant_mobile')
        email = request.POST.get('tenant_email')
        profession = request.POST.get('tenant_profession')
        house_name = request.POST.get('house_name')
        flat_no = request.POST.get('flat_no')
        room_no = request.POST.get('room_no')
        rent_amount = request.POST.get('rent_amount')
        rent_start_date = request.POST.get('rent_start_date')
        
        if not all([photo,name, address, mobile, email, rent_amount, rent_start_date]):
            return HttpResponse("Error: All fields are required except photo.", status=400)

        if not email or '@' not in email:
            return HttpResponse("Error: Invalid email address.", status=400)
        
        if not mobile.isdigit():
            return HttpResponse("Error: Mobile number should contain only digits.", status=400)

        try:
            tenant = Tenant(
                photo=photo,
                name=name,
                address=address,
                mobile=mobile,
                email=email,
                profession=profession,
                house_name=house_name,
                flat_number=flat_no,
                room_number=room_no,
                rent_amount=rent_amount,
                rent_start_date=rent_start_date,
                
            )
            tenant.save()
        except ValidationError as e:
            return HttpResponse(f"Error: {e.message}", status=400)

        return redirect('tenant_list')  
    return render(request, 'MainApp/rental.html')

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, "MainApp/tenant_list.html", {'tenants': tenants})


def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'MainApp/create_invoice.html', {'form': form})


def invoice_list(request):
    invoices = Invoice.objects.all()  
    return render(request, 'MainApp/invoice_list.html', {'invoices': invoices})


def main(request):
    return render(request, 'MainApp/m.html')


from django.urls import reverse

