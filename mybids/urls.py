from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/catalog
    path('', views.index, name="mybids-index"),
]