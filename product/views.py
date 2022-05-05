from django.shortcuts import render, get_object_or_404, redirect
from fire_sale.models import Product
# Create your views here.


def index(request):
    return render(request, 'product/index.html')


def get_product_by_id(request, id):
    product = Product.objects.get(pk=id)# select product prefetch / einhvernstaðar
    context = {
        'category': product
    }
    return render(request, 'product/index.html', context)