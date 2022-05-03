from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/firesale
    path('categories', views.index, name="categories-index"),
]