from django.contrib import messages
from django.http import HttpResponseRedirect
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
    product = Product.objects.get(pk=id)  # select product prefetch / einhvernstaðar
    form = PostBidForm()
    context = {
        'product': product,
        'form': form
    }

    if request.method == 'POST':
        form = PostBidForm(data=request.POST)
        if product.price >= int(request.POST["Amount"]):
            ''' 
            Checks for the bid amount and returns an error if it's equal
            or lower to the current amount
            '''
            messages.add_message(request, messages.INFO, 'Bid to low')
            return HttpResponseRedirect(request.path_info)
        if form.is_valid():
            '''
            Send form to update price if valid
            '''
            amount = form.cleaned_data.get('Amount')
            product_id = id
            bid_user_id = request.user.id
            bid_placed = Bids(Amount=amount, Product_id=product_id, Bid_user_id=bid_user_id)
            bid_placed.save()
            # request.method = 'GET'
            update_price(request, id, amount)
            return HttpResponseRedirect(request.path_info)
    else: #TODO taka út?
        pass
    return render(request, 'product/index.html', context)


def update_price(request, id, amount):
    '''
    Update the current amount if placed bid is larger
    '''
    product = Product.objects.get(pk=id)
    name = product.name
    description = product.description
    price = amount
    condition = product.condition
    image = product.image
    category_id = product.category_id
    seller_id = product.seller_id
    product = Product(id=id, name=name, description=description, price=price, condition=condition, image=image, category_id=category_id, seller_id=seller_id)
    product.save()
