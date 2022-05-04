from django.shortcuts import render, get_object_or_404
from categories.models import Category
# Create your views here.


def index(request):
    context = {'categories': Category.objects.all().order_by('name')}
    return render(request, 'firesale/index.html', context)
