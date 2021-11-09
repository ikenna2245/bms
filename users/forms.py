from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from bootstrap_modal_forms.forms import BSModalModelForm

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


class CustomUserChangeForm(UserChangeForm, BSModalModelForm):

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