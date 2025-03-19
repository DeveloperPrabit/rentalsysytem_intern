from django.shortcuts import render,redirect
from .forms import EditProfileForm
from django.contrib import messages



# Create your views here.

def index(request):
    return render(request,"MainApp/index.html")


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .forms import EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Profile

def edit_profile(request):
    if request.method == 'POST' and request.FILES.get:
        user = request.user
        photo = request.FILES['profile_photo']
        data=Profile(user=user,photo=photo)
        data.save()
        messages.success(request, 'Profile photo updated successfully!')
        return redirect('profile')  # Redirect to the profile page or wherever needed
    
    return render(request, 'MainApp/edit_profile.html')


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