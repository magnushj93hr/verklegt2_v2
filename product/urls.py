from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/catalog
    path('', views.index, name="product-index"),
    #path('<int:id>', views.get_product_by_id, name='product')
    path('<int:id>', views.place_bid, name='product')
]