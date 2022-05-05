from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


def get_category_by_id(request, id):
    return render(request, 'catalog/index.html', {
        #'category': get_object_or_404(Category, pk=id)
    })