from fire_sale.models import Bids
from django.forms import ModelForm, widgets


class PostBidForm(ModelForm):
    class Meta:
        model = Bids
        exclude = ['Bid_user', 'Product']
        widget = {
            'Amount': widgets.NumberInput(attrs={'class': 'form-control'})
        }

