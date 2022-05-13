from django import forms
from django.forms import ModelForm, widgets
from fire_sale.models import ContactInformation


class ContactInformationCreateForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        exclude = ['id']
        widgets = {
            'Full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'Street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'House_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'City': widgets.TextInput(attrs={'class': 'form-control'}),
            'Country': widgets.Select(attrs={'class': 'form-control'}),  # bæta við Country dropdown
            'Zip': widgets.NumberInput(attrs={'class': 'form-control'})
        }
