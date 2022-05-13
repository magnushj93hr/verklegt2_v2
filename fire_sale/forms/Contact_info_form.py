from django.forms import ModelForm, widgets
from fire_sale.models import ContactInformation


class ContactInformationCreateForm(ModelForm):
    class Meta:
        model = ContactInformation
        exclude = ['id']
        widget = {
            'Full name': widgets.TextInput(attrs={'class': 'form-control', 'name': 'fullname', 'id': 'fullname'}),
            'Street Name': widgets.TextInput(attrs={'class': 'form-control', 'name': 'streetname', 'id': 'streetname'}),
            'House number': widgets.NumberInput(attrs={'class': 'form-control', 'name': 'housenumber', 'id': 'housenumber'}),
            'City': widgets.TextInput(attrs={'class': 'form-control', 'name': 'city', 'id': 'city'}),
            'Country': widgets.TextInput(attrs={'class': 'form-control', 'name': 'country', 'id': 'country'}), # bæta við Country dropdown
            'Zip': widgets.NumberInput(attrs={'class': 'form-control', 'name': 'zip', 'id': 'zip'})
        }
