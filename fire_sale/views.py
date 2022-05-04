from django.shortcuts import render, redirect
from fire_sale.forms.product_form import ProductCreateForm

# Create your views here.
from fire_sale.models import ProductImage


def index(request):
    return render(request, 'Firesale/index.html')


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
    return render(request, 'Firesale/create_product.html', {
        'form': form
    })
