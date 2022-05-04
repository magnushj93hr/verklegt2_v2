from django.shortcuts import render, get_object_or_404
from categories.models import Category
from fire_sale.models import Product


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')

def get_category_by_id(request, id):
    context = {'product': Product.objects.all().order_by('name')}
    return render(request, 'catalog/index.html', context)

