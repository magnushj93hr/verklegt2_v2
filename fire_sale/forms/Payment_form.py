from django.forms import ModelForm, widgets, forms

from fire_sale.models import PaymentInformation


class PaymentCreateForm(ModelForm):
    class Meta:
        model = PaymentInformation
        exclude = ['id']
        widget = {
            'Name on card': widgets.TextInput(attrs={'class': 'form-control', 'name': 'cardname', 'id': 'cardname'}),
            'Card number': widgets.NumberInput(attrs={'class': 'form-control', 'name': 'cardnum', 'id': 'cardnum'}),
            'Expiration month': widgets.Select(attrs={'class': 'form-control', 'name': 'exp', 'id': 'exp'}),
            'Expiration year': widgets.NumberInput(attrs={'class': 'form-control',  'name': 'expy', 'id': 'expy'}),
            'CVC': widgets.NumberInput(attrs={'class': 'form-control',  'name': 'cvc', 'id': 'cvc'})
        }
