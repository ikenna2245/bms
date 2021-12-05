from django import forms
from users.models import CustomUser
from .models import Location, Installation, Report

class LocationForm (forms.ModelForm):
    clients = forms.ModelChoiceField(queryset=CustomUser.objects.filter(user_status='C'), widget=forms.Select(attrs={'class':'form-control','required' :True,}))
    class Meta:
        model = Location
        fields = ('clients', 'branch_id', 'state', 'address')
        widgets = {
            'branch_id': forms.TextInput(attrs={'id':'branch_id', 'required' :True, 'class':'form-control'}),
            'state' : forms.Select(attrs={'id':'state', 'required' :True, 'class':'form-control'}),
            'address': forms.TextInput(attrs={'id':'address', 'required' :True, 'class':'form-control'})
        }

class InstallationForm(forms.ModelForm):
    location = forms.ModelChoiceField(queryset=Location.objects.all(), widget=forms.Select(attrs={'class':'form-control','required' :True,}))
    engineer = forms.ModelChoiceField(queryset=CustomUser.objects.filter(user_status='E'), widget=forms.Select(attrs={'class':'form-control','required' :True,}))
    
    class Meta:
        model = Installation
        fields = ('location', 'equipment_type', 'equipment_others', 'brand_name', 'technical_specification', 'date_manufactured', 'installation_date',
                     'replacement_date', 'contact_person', 'equipment_status', 'engineer', 'remark', 'photo' )
        
        widgets = {
            'equipment_type' : forms.Select(attrs={'required' :True, 'class':'form-control'}),
            'equipment_others': forms.TextInput(attrs={'class':'form-control', 'id':'others'}),
            'brand_name' : forms.TextInput(attrs={'required' :True, 'class':'form-control'}),
            'technical_specification' : forms.TextInput(attrs={'class':'form-control'}),
            'date_manufactured': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'installation_date' : forms.DateInput(attrs={'required' :True, 'class':'form-control', 'type':'date'}),
            'replacement_date' : forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'contact_person' : forms.TextInput(attrs={'required' :True, 'class':'form-control'}),
            'equipment_status' :  forms.Select(attrs={'required' :True, 'class':'form-control'}),
            'remark' : forms.TextInput(attrs={'required' :True, 'class':'form-control'}),
            'photo': forms.FileInput(attrs={'accept':"image/*", 'class':'form-control'})
        }

class ReportForm(forms.ModelForm):
    engineer = forms.ModelChoiceField(queryset=CustomUser.objects.filter(user_status='E'), widget=forms.Select(attrs={'class':'form-control','required' :True}))
    installation = forms.ModelChoiceField(queryset=Installation.objects.all(), widget=forms.Select(attrs={'class':'form-control','required' :True}))
    class Meta:
        model = Report
        fields = ('engineer', 'installation', 'report')
        widgets = {
            'report': forms.Textarea(attrs={'class':'form-control', 'required':True})
        }