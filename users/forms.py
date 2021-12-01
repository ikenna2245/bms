from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'address','business_name', 'user_status', 'phone_number')
        widgets = {
           'email' : forms.EmailInput(attrs={'id': 'email', 'required':True, 'class':'form-control'}),
           'first_name' : forms.TextInput(attrs={'id': 'first_name', 'required':True, 'class':'form-control'}),
           'last_name' : forms.TextInput(attrs={'id': 'last_name', 'required':True, 'class':'form-control'}),
           'address' : forms.TextInput(attrs={'id': 'address', 'required':True, 'class':'form-control'}),
           'business_name' : forms.TextInput(attrs={'id': 'business_name', 'class':'form-control'}),
           'user_status': forms.Select(attrs={'id': 'user_status', 'required':True, 'class':'form-control'}),
           'phone_number' : forms.TextInput(attrs={'id': 'phone_number','required':True, 'class':'form-control'}),
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'address', 'business_name', 'user_status', 'phone_number')
        widgets = {
           'email' : forms.EmailInput(attrs={'id': 'email', 'required':True, 'class':'form-control'}),
           'first_name' : forms.TextInput(attrs={'id': 'first_name', 'required':True, 'class':'form-control'}),
           'last_name' : forms.TextInput(attrs={'id': 'last_name', 'required':True, 'class':'form-control'}),
           'address' : forms.TextInput(attrs={'id': 'address', 'required':True, 'class':'form-control'}),
           'business_name' : forms.TextInput(attrs={'id': 'business_name', 'class':'form-control'}),
           'user_status': forms.Select(attrs={'id': 'user_status', 'required':True, 'class':'form-control'}),
           'phone_number' : forms.TextInput(attrs={'id': 'phone_number','required':True, 'class':'form-control'}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    
    class Meta:
        model: CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')
        wiidget = {
            'old_password': forms.PasswordInput(attrs={'id': 'old_password', 'name':'old_password', 'required':True, 'class':'form-control'}),
            'new_password1': forms.PasswordInput(attrs={'id': 'new_password1', 'name':'new_password1', 'required':True, 'class':'form-control'}),
            'new_password2': forms.PasswordInput(attrs={'id': 'new_password2', 'name':'new_password2', 'required':True, 'class':'form-control'})
        }