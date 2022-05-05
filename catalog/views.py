from django.shortcuts import render, get_object_or_404
from fire_sale.models import ProductCategory
from fire_sale.models import Product


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


def get_category_by_id(request, id):
    category = ProductCategory.objects.get(pk=id)# select product prefetch / einhvernstaðar
    context = {
        'category': category
    }
    return render(request, 'Catalog/index.html', context)
