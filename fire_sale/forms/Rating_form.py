from django.forms import ModelForm, widgets
from fire_sale.models import Rating


class RatingForm(ModelForm):

    class Meta:
        exclude = ['user']
        model = Rating
        widgets = {
            'Grade': widgets.TextInput(attrs={'class': 'form-control'})
        }
