from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/firesale
    path('', views.index, name="Firesale-index"),
    path('create_product', views.create_product, name="create_product"),
    path('get_prodcut_by_seller_id', views.get_product_by_seller_id, name="my_listings"),
    path('get_my_bids', views.get_my_bids, name="my_bids"),
]
