from django.shortcuts import render, get_object_or_404
from categories.models import Category
from fire_sale.models import Product

# Create your views here.
def index(request):
    context = {'product': Product.objects.all().order_by('name')}
    return render(request, 'catalog/index.html', context)


def get_category_by_id(request, id):
    return render(request, 'catalog/index.html', {
        'category': get_object_or_404(Category, pk=id)
    })