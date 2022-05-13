from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/catalog
    path('', views.index, name="product-index"),
    path('<int:id>', views.place_bid, name='product'),
    path('add_to_favorite', views.add_to_favorite, name='add_to_favorite')
]
