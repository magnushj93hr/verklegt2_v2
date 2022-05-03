from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/firesale
    path('', views.index, name="myprofile-index"),
]