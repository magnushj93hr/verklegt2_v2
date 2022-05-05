from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/firesale
    path('', views.index, name="Firesale-index"),
    path('create_product', views.create_product, name="create_product")
]
