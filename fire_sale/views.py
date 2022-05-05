from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from fire_sale.models import ProductCategory
from fire_sale.forms.product_form import ProductCreateForm
from fire_sale.models import ProductImage


def index(request):
    context = {'categories': ProductCategory.objects.all().order_by('name')}
    return render(request, 'firesale/index.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            product_image.save()
            return redirect('Firesale-index')
    else:
        form = ProductCreateForm()
    return render(request, 'firesale/create_product.html', {
        'form': form
        })
