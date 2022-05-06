from django.shortcuts import render, get_object_or_404, redirect
from fire_sale.models import Product
from product.forms.bid_form import PostBidForm
# Create your views here.


def index(request):
    return render(request, 'product/index.html')


def get_product_by_id(request, id):
    product = Product.objects.get(pk=id)# select product prefetch / einhvernstaðar
    context = {
        'product': product
    }
    return render(request, 'product/index.html', context)


def place_bid(request, id):
    product = Product.objects.get(pk=id)  # select product prefetch / einhvernstaðar
    context = {
        'product': product,
    }
    if request.method == 'POST':
        form = PostBidForm(data=request.POST)
        if form.is_valid():
            return redirect('Firesale-index')
    else:
        form = PostBidForm()
    return render(request, 'product/index.html', context)
