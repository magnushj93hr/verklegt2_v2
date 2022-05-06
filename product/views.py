from django.shortcuts import render, get_object_or_404, redirect
from fire_sale.models import Product, Bids
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
    print(request)
    product = Product.objects.get(pk=id)  # select product prefetch / einhvernstaðar
    form = PostBidForm()
    context = {
        'product': product,
        'form': form
    }
    if request.method == 'POST':
        form = PostBidForm(data=request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('Amount')
            product_id = id
            bid_user_id = request.user.id
            bid_placed = Bids(Amount=amount, Product_id=product_id, Bid_user_id=bid_user_id)
            bid_placed.save()
            return redirect('/')
    else:
        pass # form = PostBidForm()
    return render(request, 'product/index.html', context)
