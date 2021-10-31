from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm (UserCreationForm):
    first_name = forms.CharField(max_length= 64, required = True, widget=forms.TextInput(attrs={'id': 'first_name', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length= 64, required = True, widget=forms.TextInput(attrs={'id': 'last_name', 'placeholder':'Last Name'}))
    password1 = forms.CharField(max_length=16, required = True, widget=forms.PasswordInput(attrs={'id': 'password1', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, required = True, widget=forms.PasswordInput(attrs={'id': 'password2', 'placeholder': 'Confirm Password'}))
    country = forms.CharField(max_length= 120, required = True, widget=forms.TextInput(attrs={'id': 'form-control', 'placeholder':'Country'}))
    state = forms.CharField(max_length=55, required=True, widget=forms.TextInput(attrs={'id':'state', 'placeholder': 'State'}))
    address = forms.CharField(max_length=500, required=True, widget=forms.TextInput(attrs={'id': "address", "placeholder": "Enter Address"}))
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", 
                    "last_name", "referral", "country", "zipcode",
                     "state", "address", "ltc", "btc", "eth", 'paypal']
        widgets = {
        'email' : forms.EmailInput(attrs={'id': 'email', 'required':True, 'placeholder':'user@email.com'}),
        'username' : forms.TextInput(attrs={'id': 'username', 'required':True, 'placeholder':'Username'})
        }

class UserUpdateForm (UserCreationForm):
    first_name = forms.CharField(max_length= 64, widget=forms.TextInput(attrs={'id': 'first_name', 'placeholder':'First Name', 'readonly':True}))
    last_name = forms.CharField(max_length= 64, widget=forms.TextInput(attrs={'id': 'last_name', 'placeholder':'Last Name', 'readonly':True}))
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        widgets = {
        'email' : forms.EmailInput(attrs={'id': 'email', 'readonly':True}),
        'username' : forms.TextInput(attrs={'id': 'username', 'readonly':True,})
        }


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model= Profile
        fields = ["address", "image", "phone_number", "zipcode", "state", "country", "bitcoin_wallet", "ethereum_wallet", "paypal_email", "litecoin_wallet"]
