from django.forms import ModelForm, widgets
from fire_sale.models import Rating


class RatingForm(ModelForm):
    model = Rating
    exclude = ['user']

    class Meta:
        widget = {
            'Rating (1-10)': widgets.Select(attrs={'class': 'form-control'})
        }
