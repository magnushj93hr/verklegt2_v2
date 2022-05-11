from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from fire_sale.forms.Rating_form import RatingForm
from fire_sale.forms.Contact_info_form import ContactInformationCreateForm
from fire_sale.forms.Payment_form import PaymentCreateForm
from fire_sale.models import ProductCategory, Product, ContactInformation, PaymentInformation, Bids, Rating, \
    Notification
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
    new_value = request.GET.get('id')
    if new_value:
        request.session['product_id'] = new_value
    if request.method == 'POST':
        form = ContactInformationCreateForm(data=request.POST)
        if form.is_valid():
            request.session['Full_name'] = form.cleaned_data.get('Full_name')
            request.session['Street_name'] = form.cleaned_data.get('Street_name')
            request.session['House_number'] = form.cleaned_data.get('House_number')
            request.session['City'] = form.cleaned_data.get('City')
            request.session['Country'] = form.cleaned_data.get('Country')
            request.session['Zip'] = form.cleaned_data.get('Zip')
        # for key, value in request.session.items():
        #    print('{} => {}'.format(key, value))
        # contact_information = ContactInformation(full_name=full_name, street_name=street_name,
        #                                         house_number=house_number, city=city, country=country, zip=zip)
        # contact_information.save()
        # print(contact_information)
        # get_payment_information(request)
        return redirect('payment_information')
    else:
        form = ContactInformationCreateForm()
    return render(request, 'firesale/contact_information.html', {
        'form': form
    })


def get_payment_information(request):
    if request.method == 'POST':
        form = PaymentCreateForm(data=request.POST)
        if form.is_valid():
            request.session['Name_of_cardholder'] = form.cleaned_data.get('Name_of_cardholder')
            request.session['card_number'] = form.cleaned_data.get('card_number')
            request.session['Exp_month'] = form.cleaned_data.get('Exp_month')
            request.session['Exp_year'] = form.cleaned_data.get('Exp_year')
            request.session['CVC'] = form.cleaned_data.get('CVC')
            # for key, value in request.session.items():
            #    print('{} => {}'.format(key, value))
            # payment_information = PaymentInformation(name_of_cardholder=name_of_cardholder, card_number=card_number,
            #                                         exp_month=exp_month, exp_year=exp_year, cvc=cvc)
            # payment_information.save()
        return redirect('view_payment')
        # return render(request, 'firesale/view_payment.html')  # gera post skjá með upplýsingum
    else:
        form = PaymentCreateForm()
    return render(request, 'firesale/payment_information.html', {
        'form': form
    })


def view_payment(request):
    if request.method == 'GET':
        return render(request, 'firesale/view_payment.html')
    elif request.method == 'POST':
        name_of_cardholder = request.session['Name_of_cardholder']
        card_number = request.session['card_number']
        exp_month = request.session['Exp_month']
        exp_year = request.session['Exp_year']
        cvc = request.session['CVC']
        payment = PaymentInformation(Name_of_cardholder=name_of_cardholder, card_number=card_number,
                                     Exp_month=exp_month, Exp_year=exp_year, CVC=cvc)
        payment.save()
        full_name = request.session['Full_name']
        street_name = request.session['Street_name']
        house_number = request.session['House_number']
        city = request.session['City']
        country = request.session['Country']
        zip = request.session['Zip']
        contact_information = ContactInformation(Full_name=full_name, Street_name=street_name,
                                                 House_number=house_number, City=city, Country=country, Zip=zip)
        contact_information.save()
        product_id = request.session['product_id']
        update_payment(request, product_id)
        return redirect('rating_view')


def rating_view(request):
    if request.method == 'POST':
        form = RatingForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            grade = form.cleaned_data.get('Grade')
            user_id = request.user.id
            rating = Rating(Grade=grade, user_id=user_id)
            rating.save()
            return redirect('Firesale-index')
    else:
        form = RatingForm()
    return render(request, 'firesale/give_rating.html',{
            'form': form
        })


def update_payment(request, id):
    product = Product.objects.get(pk=id)
    name = product.name
    description = product.description
    price = product.price
    condition = product.condition
    image = product.image
    category_id = product.category_id
    seller_id = product.seller_id
    accept = product.accepted
    payment = True
    product = Product(id=id, name=name, description=description, price=price, condition=condition, image=image,
                      category_id=category_id, seller_id=seller_id, accepted=accept, payment=payment)
    product.save()


def get_product_by_seller_id(request):
    seller = request.user.id
    product = Product.objects.filter(seller_id=seller)
    for p in product:
        p.__setattr__("bids", Bids.objects.filter(Product_id=p.id))
        print(p.bids)
    context = {
        'product': product
    }
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        product = Product.objects.get(pk=prod_id)
        context = {
            'product': product
        }
        bidders = set()
        buyer_email = ""
        products = Bids.objects.filter(Product_id=prod_id)

        buyer_id = ""
        for prod in products:
            if prod.Amount == product.price:
                buyer_id = prod.Bid_user_id
        for prod in products:
            if prod.Bid_user_id != buyer_id:
                bidders.add(prod.Bid_user_id)

        notification = Notification(seen=False,
                                    message="Your bid has been accepted, please proceed to My Bids for payment",
                                    buyer_id=buyer_id, product_id=product.id)
        notification.save()
        for bidder in bidders:
            not_accepted_not = Notification(seen=False, message="Your bid has not been accepted", buyer_id=bidder,
                                            product_id=product.id)
            not_accepted_not.save()
        push_notification(request) #hafa með eða ekki??

        update_accept(request, prod_id)

        return render(request, 'firesale/message_after_accepted.html', context)

    return render(request, 'firesale/my_listings.html', context)


def push_notification(request):
    user_id = request.user.id
    notifications = Notification.objects.filter(buyer_id=user_id)
    for notif in notifications:
        notif.__setattr__('Product', Product.objects.filter(id=notif.product_id))

    context = {
        'notifications': notifications,
    }
    return render(request, 'firesale/notifications.html', context)


def update_accept(request, id):
    product = Product.objects.get(pk=id)
    name = product.name
    description = product.description
    price = product.price
    condition = product.condition
    image = product.image
    category_id = product.category_id
    seller_id = product.seller_id
    accept = True
    product = Product(id=id, name=name, description=description, price=price, condition=condition, image=image,
                      category_id=category_id, seller_id=seller_id, accepted=accept)
    product.save()


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
        # 'bids': bids,
        'product': product_list
    }
    if request.method == 'POST':
        get_contact_information(request)
        # return render(request, 'firesale/contact_information.html')
    return render(request, 'firesale/listbids.html', context)
