from django.forms import ModelForm, widgets, forms

from fire_sale.models import Payment


class PaymentCreateForm(ModelForm):
    class Meta:
        model = Payment
        widget = {
            'Name on card': widgets.TextInput(attrs={'class': 'form-control'}),
            'Expiration month': widgets.Select(attrs={'class': 'form-control'}),
            'Expiration year': widgets.NumberInput(attrs={'class': 'form-control'}),
            'CVC': widgets.NumberInput(attrs={'class': 'form-control'})
        }
