from django.shortcuts import render
from MainApp.models import RentInvoice,Invoice
from.models import CustomUser
from django.shortcuts import render,redirect,get_object_or_404
from MainApp.forms import InvoiceForm

def view_users(request):
    users = CustomUser.objects.filter(is_superuser=False) 
    return render(request, 'Dashboard/view_users.html', {'users': users})


def manage_user(request):
    users = CustomUser.objects.filter(is_superuser=False) 
    return render(request, 'Dashboard/manage_user.html', {'users': users})

def view_tenant(request):
    rent_invoices = RentInvoice.objects.all()
    context = {
        'rent_invoices': rent_invoices  
    }
    return render(request, 'Dashboard/view_tenant.html', context)

def manage_tenant(request):
    tenants = RentInvoice.objects.all()

    return render(request, 'Dashboard/manage_tenant.html',{'tenants': tenants})


def view_invoice(request):
    invoices = Invoice.objects.all().order_by('tenant__tenant_name', 'total_amount')  
    return render(request, 'Dashboard/view_invoices.html', {'invoices': invoices})

def manage_invoices(request):
    invoices = Invoice.objects.all().order_by('tenant__tenant_name')  
    return render(request, 'Dashboard/manage_invoices.html',{'invoices':invoices})

def change_password(request):
    return render(request, 'Dashboard/password_change.html')

def delete_invoices(request, id):
    data=Invoice.objects.get(id=id)    
    data.delete()
    
    return redirect('view_invoices')



def edit_invoice(request, id):
    invoice = get_object_or_404(Invoice, id=id)
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('view_invoices')
    else:
        form = InvoiceForm(instance=invoice)  

    return render(request, 'Dashboard/edit_invoices.html', {'form': form})


def delete_user(request, id):
    user = get_object_or_404(CustomUser, id=id)
    
    if not request.user.is_superuser:
        return redirect('view_users')
    if request.method == 'POST':
        user.delete()  
        return redirect('view_users')  