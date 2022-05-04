from django.shortcuts import render
from categories.models import Category
# Create your views here.

def index(request):
    context = {'categories': Category.objects.all().order_by('name')}
    return render(request, 'firesale/index.html', context)