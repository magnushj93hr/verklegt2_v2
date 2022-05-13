from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from fire_sale.models import Product, Bids, Favourites
from product.forms.bid_form import PostBidForm


# Create your views here.


def index(request):
    return render(request, 'product/index.html')


def get_product_by_id(request, id):
    product = Product.objects.get(pk=id)  # select product prefetch / einhvernstaðar
    print(product)
    context = {
        'product': product
    }
    return render(request, 'product/index.html', context)


def place_bid(request, id):
    product = Product.objects.get(pk=id)  # select product prefetch / einhvernstaðar
    other_products = Product.objects.filter(category_id=product.category_id)  # þarf að mínusa frá þá vöru sem er...
    other_products2 = other_products.filter(accepted=False)
    other_products3 = other_products2.exclude(id=product.id)[:3]
    form = PostBidForm()
    context = {
        'product': product,
        'similarproducts': other_products3,
        'form': form
    }

    if request.method == 'POST':
        if product.seller_id == request.user.id:  # Bæta bið pop up eða eitthvað slíkt
            messages.add_message(request, messages.INFO, 'Thats your own bid!')
            return HttpResponseRedirect(request.path_info)
        form = PostBidForm(data=request.POST)
        if product.price >= int(request.POST["Amount"]):
            ''' 
            Checks for the bid amount and returns an error if it's equal
            or lower to the current amount
            '''
            messages.add_message(request, messages.INFO, 'Bid to low')
        elif form.is_valid():
            '''
            Send form to update price if valid
            '''
            amount = form.cleaned_data.get('Amount')
            product_id = id
            bid_user_id = request.user.id
            bid_placed = Bids(Amount=amount, Product_id=product_id, Bid_user_id=bid_user_id)
            bid_placed.save()
            # request.method = 'GET'
            update_price(request, id, amount, bid_user_id)
            return render(request, 'product/message_after_placebid.html', context)

    return render(request, 'product/index.html', context)


def update_price(request, id, amount, bid_user_id):
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
    buyer_id = bid_user_id
    product = Product(id=id, name=name, description=description, price=price, condition=condition, image=image,
                      category_id=category_id, seller_id=seller_id,
                      highest_bidder=buyer_id)
    product.save()


def add_to_favorite(request):
    retrieved_items = request.POST.get('product_id')
    product_id, old_path = retrieved_items.split(',')
    user_id = request.user
    items = Favourites.objects.filter(user_id=user_id)
    items2 = items.filter(product_id=product_id)
    print(old_path)
    if items2:
        items2.delete()
    else:
        Favourites.objects.create(product_id=product_id, user=user_id)
    return redirect('favorites')
