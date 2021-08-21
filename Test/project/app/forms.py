from django import forms
from .models import *

class PayForm(forms.ModelForm):
    class Meta:
        model = Payslip
        fields = '__all__'
        #fields = ['name','address','pan','uan','basic_pay','benefites']

        labels = {
            'name': '',
            'address': '',
            'pan': '',
            'uan': '',
            'basic_pay': '',
            'benefites': '',
            'Taxes' : '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'pan': forms.TextInput(attrs={'class':'form-control','placeholder':'PAN Number'}),
            'uan': forms.TextInput(attrs={'class':'form-control','placeholder':'UAN Number'}),
            'basic_pay': forms.TextInput(attrs={'class':'form-control','placeholder':'Basic Pay'}),
            'benefites': forms.TextInput(attrs={'class':'form-control','placeholder':'Benifits'}),
            'Taxes' : forms.TextInput(attrs={'class':'form-control','placeholder':'Tax amount','disabled': True}),
        }

        """widgets = {
        'Taxes': forms.TextInput(attrs={'disabled': True}),
        }"""

class TaxForm(forms.ModelForm):
    class Meta:
        model = SetTaxes
        fields = '__all__'

        labels = {
            'taxPercent' : ''
        }

        widgets = {
            'taxPercent' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tax Percentage'})
        }