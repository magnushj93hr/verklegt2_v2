from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/firesale
    path('', views.index, name="Firesale-index"),
    path('create_product', views.create_product, name="create_product"),
    path('get_prodcut_by_seller_id', views.get_product_by_seller_id, name="my_listings"),
    path('get_my_bids', views.get_my_bids, name="my_bids"),
    path('get_contact_information', views.get_contact_information, name="contact_information"),
    path('get_payment_information', views.get_payment_information, name="payment_information"),
    path('view_payment', views.view_payment, name="view_payment"),
    path('rating_view', views.rating_view, name="rating_view"),
    path('push_notification', views.push_notification, name='push_notification'),
]
