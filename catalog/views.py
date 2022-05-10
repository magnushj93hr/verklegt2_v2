from django.shortcuts import render, get_object_or_404
from fire_sale.models import ProductCategory
from fire_sale.models import Product


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


def get_category_by_id(request, id):
    if request.GET['sort_by'] == "price":
        product = Product.objects.filter(category_id=id).order_by('price')
    elif request.GET['sort_by'] == 'name':
        product = Product.objects.filter(category_id=id).order_by('name')
    req = request.GET.copy()
    print(req)
    category = ProductCategory.objects.get(pk=id)# select product prefetch / einhvernstaðar
    context = {
        'category': category,
        'product': product
    }
    return render(request, 'Catalog/index.html', context)


