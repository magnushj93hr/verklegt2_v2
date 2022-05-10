from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

from fire_sale.forms.Contact_info_form import ContactInformationCreateForm
from fire_sale.forms.Payment_form import PaymentCreateForm
from fire_sale.models import ProductCategory, Product, ContactInformation, PaymentInformation, Bids
from fire_sale.forms.product_form import ProductCreateForm
from fire_sale.models import ProductImage
from fire_sale.models import Product
from django.core.mail import send_mail


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'price': x.price,
            'image': x.image,

        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    product = Product.objects.all()
    category = ProductCategory.objects.all().order_by('name')
    context = {
        'categories': category,
        'product': product
    }
    return render(request, 'firesale/index.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            price = form.cleaned_data.get('price')
            condition = form.cleaned_data.get('condition')
            image = form.cleaned_data.get('image')
            seller = request.user

            product = Product(name=name, description=description, category=category, price=price, condition=condition,
                              image=image, seller=seller)
            product.save()
            # product = form.save()
            product_image = ProductImage(image=image, product=product)
            product_image.save()
            # seller = form.save()
            # seller.save()
            return redirect('Firesale-index')
    else:
        form = ProductCreateForm()
    return render(request, 'firesale/create_product.html', {
        'form': form
    })


def get_contact_information(request):
    if request.method == 'POST':
        form = ContactInformationCreateForm(data=request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            street_name = form.cleaned_data.get('street_name')
            house_number = form.cleaned_data.get('house_number')
            city = form.cleaned_data.get('city')
            country = form.cleaned_data.get('country')
            zip = form.cleaned_data.get('zip')

            contact_information = ContactInformation(Full_name=full_name, Street_Name=street_name,
                                                     House_number=house_number, City=city, Country=country, Zip=zip)
            contact_information.save()
            return redirect('firesale/payment_information.html')
    else:
        form = ContactInformationCreateForm()
    return render(request, 'firesale/contact_information.html', {
        'form': form
    })


def get_payment_information(request):
    if request.method == 'POST':
        form = PaymentCreateForm(data=request.POST)
        if form.is_valid():
            name_of_cardholder = form.cleaned_data.get('Name_of_cardholder')
            card_number = form.cleaned_data.get('card_number')
            exp_month = form.cleaned_data.get('Exp_month')
            exp_year = form.cleaned_data.get('Exp_year')
            cvc = form.cleaned_data.get('CVC')

            payment_information = PaymentInformation(name_of_cardholder=name_of_cardholder, card_number=card_number,
                                                     exp_month=exp_month, exp_year=exp_year, cvc=cvc)
            payment_information.save()
            return redirect('firesale-index.html')  # gera post skjá með upplýsingum
    else:
        form = PaymentCreateForm()
    return render(request, 'firesale/payment_information.html', {
        'form': form
    })


def get_product_by_seller_id(request):
    seller = request.user.id
    product = Product.objects.filter(seller_id=seller)
    print("hello")
    for p in product:
        p.__setattr__("bids", Bids.objects.filter(Product_id=p.id))
        print(p.bids)
    context = {
        'product': product
    }
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        product = Product.objects.get(pk=prod_id)
        buyer_email = ""
        products = Bids.objects.filter(Product_id=prod_id)
        # gera if setningu ef það er engin prod í products:
        for prod in products:
            if prod.Amount == product.price:
                buyer_id = prod.Bid_user_id

        buyer = User.objects.get(pk=buyer_id)
        buyer_email = buyer.email
        send_mail(
            'Bid accepted',  # subject
            'Your bid has been accepted. Please go to my bids to continue to payment.',  # message
            'firesale@firesale.com',
            [buyer_email],
            False,
            None,
            None,
            None,
            None
        )

    return render(request, 'firesale/my_listings.html', context)


# þarf að ná í id-ið af vörunni
# þarf að finna kaupandann sem er með hæsta boðið.
## þurfum að gera þannig að það sé ekki hægt að bidda sama verð
# gera ef product id er ekki í bids þá ekki setja takkann.
# appenda emailum í lista til að senda multiples


# HVERNIG GET ÉG GERT IF SKIPUN SEM ER FYRIR EF ÞETTA PRODUCT ID ER I BIDS FILENUM?
# REGISTRATION FORM SETJA EMAIL
# GET EKKI SEARCHAÐ ÞEGAR EG ER INNI MY LISTINGS


def get_my_bids(request):
    highest_bids = set()
    user = request.user.id
    bids = Bids.objects.filter(Bid_user_id=user).values()
    for item in bids:
        id, amount, bid_user_id, product_id = item.items()
        highest_bids.add(product_id[1])
    product_list = []
    for i in highest_bids:
        product = Product.objects.filter(id=i)
        for elem in product:
            product_list.append(elem)

    context = {
        'bids': bids,
        'product': product_list
    }
    return render(request, 'firesale/listbids.html', context)
