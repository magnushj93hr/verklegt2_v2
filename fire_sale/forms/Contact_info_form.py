from django.forms import ModelForm, widgets
from fire_sale.models import ContactInformation


class ContactInformationCreateForm(ModelForm):
    class Meta:
        model = ContactInformation
        exclude = ['id']
        widget = {
            'Full name': widgets.TextInput(attrs={'class': 'form-control'}),
            'Street Name': widgets.TextInput(attrs={'class': 'form-control'}),
            'House number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'City': widgets.TextInput(attrs={'class': 'form-control'}),
            'Country': widgets.TextInput(attrs={'class': 'form-control'}), # bæta við Country dropdown
            'Zip': widgets.NumberInput(attrs={'class': 'form-control'})
        }