from fire_sale.models import Bids
from django.forms import ModelForm, widgets


class PostBidForm(ModelForm):
    class Meta:
        model = Bids
        exclude = ['id', 'product_id', 'bid_user_id']
        widget = {
            'amount': widgets.NumberInput(attrs={'class': 'form-control'})
        }