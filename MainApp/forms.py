from django import forms
from django.contrib.auth.models import User

class EditProfileForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100, required=True)
    full_address = forms.CharField(max_length=255, required=True)
    mobile = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['full_name', 'full_address', 'email', 'mobile']
