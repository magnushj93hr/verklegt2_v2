from django.contrib.auth.models import User
from django.db import models
from fire_sale.models import Rating


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)
    bio = models.CharField(max_length=9999)
    avg = models.CharField(
        max_length=4,
        default=0,
    )
