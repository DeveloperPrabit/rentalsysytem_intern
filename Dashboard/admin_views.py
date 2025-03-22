from django.shortcuts import render

def view_users(request):
    return render(request, 'Dashboard/view_users.html')

def manage_user(request):
    return render(request, 'Dashboard/manage_user.html')

def view_tenant(request):
    return render(request, 'Dashboard/view_tenant.html')

def manage_tenant(request):
    return render(request, 'Dashboard/manage_tenant.html')

def view_invoices(request):
    return render(request, 'Dashboard/view_invoices.html')

def manage_invoices(request):
    return render(request, 'Dashboard/manage_invoices.html')

def change_password(request):
    return render(request, 'Dashboard/password_change.html')