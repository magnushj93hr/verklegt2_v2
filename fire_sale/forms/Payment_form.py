from django.forms import ModelForm, widgets, forms

from fire_sale.models import PaymentInformation


class PaymentCreateForm(ModelForm):
    class Meta:
        model = PaymentInformation
        exclude = ['id']
        widget = {
            'Name on card': widgets.TextInput(attrs={'class': 'form-control'}),
            'Card number': widgets.TextInput(attrs={'class': 'form-control'}),
            'Expiration month': widgets.Select(attrs={'class': 'form-control'}),
            'Expiration year': widgets.NumberInput(attrs={'class': 'form-control'}),
            'CVC': widgets.NumberInput(attrs={'class': 'form-control'})
        }
