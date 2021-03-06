from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from fire_sale.models import Product
from django import forms


class ProductCreateForm(forms.ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    seller = User.username

    class Meta:
        model = Product
        exclude = ['id', 'seller', 'accepted', 'payment', 'highest_bidder']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'condition': widgets.Select(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'})

        }
