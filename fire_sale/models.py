from django.db import models
from categories.models import Category

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=255)
    Bio = models.CharField(max_length=255)
    image = models.CharField(max_length=9999)


class Product(models.Model):
    NEW = 'NE'
    PREOWNED = 'PO'
    CONDITON_CHOICES = [
        (NEW, 'New'),
        (PREOWNED, 'Pre Owned'),
    ]
    condition = models.CharField(
        max_length=2,
        choices=CONDITON_CHOICES,
        default=NEW,
    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=9999)
    seller = models.ForeignKey(Users, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Rating(models.Model):
    Grade = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), unique=True)
    Reviews = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)


class Bids(models.Model):
    Amount = models.IntegerField()
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

