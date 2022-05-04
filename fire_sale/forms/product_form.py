from django.forms import ModelForm, widgets
from fire_sale.models import Product
from django import forms


class ProductCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        exclude = ['id']
        widget = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            # 'users': widgets.Select(attrs={'class': 'form-control'}),
            'condition': widgets.Select(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }
