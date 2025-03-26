from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Invoice
from .models import Profile,RentInvoice
from .forms import InvoiceForm
from django.shortcuts import render, redirect
from .models import RentInvoice
import uuid 


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


def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            tenant = form.cleaned_data['tenant']
            if not RentInvoice.objects.filter(id=tenant.id).exists():
                form.add_error('tenant', 'Selected tenant does not exist.')
            else:
                form.save()
                return redirect('invoice_list')
    else:
        form = InvoiceForm()
    
    return render(request, 'MainApp/create_invoice.html', {'form': form})

def invoice_list(request):
    invoices = Invoice.objects.all()  
    return render(request, 'MainApp/invoice_list.html', {'invoices': invoices})

def tenant_list(request):
    tenants = RentInvoice.objects.all()
    return render(request, "MainApp/tenant_list.html", {'tenants': tenants})

def add_form(request):
    if request.method == "POST":
        serial_number = request.POST.get("serial_number") or str(uuid.uuid4())[:8]  
        rent_month = request.POST.get("rent_month")
        date = request.POST.get("date")
        tenant_name = request.POST.get("tenant_name")
        house_number = request.POST.get("house_no")
        flat_number = request.POST.get("flat_no")
        room_no = request.POST.get("room_no")
        building_name = request.POST.get("building_name")
        rent_amount = request.POST.get("rent_amount")
        parking_fee = request.POST.get("parking_fee")
        electricity_fee = request.POST.get("electricity_fee")
        security_fee = request.POST.get("security_fee")
        discount = request.POST.get("discount")
        total_amount = request.POST.get("total_amount")
        tax = request.POST.get("tax")
        grand_total = request.POST.get("grand_total")
        bank_name = request.POST.get("bank_name")
        account_number = request.POST.get("account_no")
        account_name = request.POST.get("account_name")
        owner_signature = request.POST.get("owner_signature")
        tenant_signature = request.POST.get("tenant_signature")

        if not serial_number or not rent_month or not date or not tenant_name:
            messages.error(request, "कृपया सबै अनिवार्य फिल्डहरू भर्नुहोस्।")
            return redirect('add_form')

        try:
            rent_amount = float(rent_amount)
        except ValueError:
            messages.error(request, "कृपया वैध बहाल रकम प्रविष्ट गर्नुहोस्।")  
            return redirect('add_form')

        try:
            total_amount = float(total_amount)
        except ValueError:
            messages.error(request, "कृपया वैध कुल रकम प्रविष्ट गर्नुहोस्।")  

        try:
            discount = float(discount) if discount else 0
        except ValueError:
            messages.error(request, "कृपया वैध छुट रकम प्रविष्ट गर्नुहोस्।")
            return redirect('add_form')

        try:
            grand_total = float(grand_total)
        except ValueError:
            messages.error(request, "कृपया वैध कुल जम्मा रकम प्रविष्ट गर्नुहोस्।")
            return redirect('add_form')

        invoice = RentInvoice.objects.create(
            serial_number=serial_number,
            rent_month=rent_month,
            date=date,
            tenant_name=tenant_name,
            house_number=house_number,
            flat_number=flat_number,
            room_no=room_no,
            building_name=building_name,
            rent_amount=rent_amount,
            parking_fee=parking_fee,
            electricity_fee=electricity_fee,
            security_fee=security_fee,
            discount=discount,
            total_amount=total_amount,
            tax=tax,
            grand_total=grand_total,
            bank_name=bank_name,
            account_number=account_number,
            account_name=account_name,
            owner_signature=owner_signature,
            tenant_signature=tenant_signature,
        )

        invoice.save()

        messages.success(request, "रेंट बिल सफलतापूर्वक थपियो!")
        return redirect('add_form')

    return render(request, "MainApp/add_form.html")
