from django import forms
from users.models import CustomUser
from .models import Location, Installation, Report

class LocationForm (forms.ModelForm):
    #clients = forms.ModelChoiceField(queryset=CustomUser.objects.filter(user_status='C'), widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Location
        fields = ('branch', 'branch_id', 'cug_num1', 'cug_num2',  'state', 'address', 'regional_office', 'region')
        widgets = {
            'branch': forms.TextInput(attrs={'id':'branch', 'required' :True, 'class':'form-control'}),
            'branch_id': forms.TextInput(attrs={'id':'branch_id', 'required' :True, 'class':'form-control'}),
            'cug_num1': forms.TextInput(attrs={'id':'cug_num1', 'class':'form-control'}),
            'cug_num2': forms.TextInput(attrs={'id':'cug_num2', 'class':'form-control'}),
            'state' : forms.Select(attrs={'id':'state', 'required' :True, 'class':'form-control'}),
            'address': forms.TextInput(attrs={'id':'address', 'required' :True, 'class':'form-control'}),
            'regional_office': forms.CheckboxInput(),
            'region' : forms.Select(attrs={'id':'region', 'required' :True, 'class':'form-control'}),
            
        }

class InstallationForm(forms.ModelForm):
    location = forms.ModelChoiceField(queryset=Location.objects.all(), widget=forms.Select(attrs={'class':'form-control','required' :True,}))
    #engineer = forms.ModelChoiceField(queryset=CustomUser.objects.filter(user_status='E'), widget=forms.Select(attrs={'class':'form-control','required' :True,}))
    
    class Meta:
        model = Installation
        fields = ('location', 'equipment_type', 'equipment_others', 'brand_name','brand_others', 'quantity', 'technical_specification','life_span', 'date_manufactured', 'installation_date',
                     'replacement_date', 'equipment_status', 'remark', 'photo' )
        
        widgets = {
            'equipment_type' : forms.Select(attrs={'required' :True, 'class':'form-control'}),
            'equipment_others': forms.TextInput(attrs={'class':'form-control', 'id':'others'}),
            'brand_name' : forms.Select(attrs={'required' :True, 'class':'form-control'}),
            'brand_others': forms.TextInput(attrs={'class':'form-control', 'id':'brand_others'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control'}),
            'technical_specification' : forms.TextInput(attrs={'class':'form-control'}),
            'life_span': forms.Select(attrs={'class':'form-control'}),
            'date_manufactured': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'installation_date' : forms.DateInput(attrs={'required' :True, 'class':'form-control', 'type':'date'}),
            'replacement_date' : forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            #'contact_person' : forms.TextInput(attrs={'required' :True, 'class':'form-control'}),
            'equipment_status' :  forms.Select(attrs={'required' :True, 'class':'form-control'}),
            'remark' : forms.TextInput(attrs={'required' :True, 'class':'form-control'}),
            'photo': forms.FileInput(attrs={'accept':"image/*", 'class':'form-control'})
        }

class ReportForm(forms.ModelForm):
    #engineer = forms.ModelChoiceField(queryset=CustomUser.objects.filter(user_status='E'), widget=forms.Select(attrs={'class':'form-control','required' :True}))
    installation = forms.ModelChoiceField(queryset=Installation.objects.all(), widget=forms.Select(attrs={'class':'form-control','required' :True}))
    class Meta:
        model = Report
        fields = ('installation', 'report')
        widgets = {
            'report': forms.Textarea(attrs={'class':'form-control', 'required':True})
        }