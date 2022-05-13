from django.forms import ModelForm, widgets, forms
from fire_sale.models import PaymentInformation


class PaymentCreateForm(ModelForm):
    class Meta:
        model = PaymentInformation
        exclude = ['id']
        widgets = {
            'Name_of_cardholder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'Exp_month': widgets.Select(attrs={'class': 'form-control'}),
            'Exp_year': widgets.NumberInput(attrs={'class': 'form-control'}),
            'CVC': widgets.NumberInput(attrs={'class': 'form-control'})
        }
