from django.db import models
from categories.models import Category


# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    image = models.CharField(max_length=9999)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    NEW = 'NE'
    PREOWNED = 'PO'
    COND_CHOICES = [
        (NEW, 'New'),
        (PREOWNED, 'Pre Owned'),
    ]
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    seller = models.ForeignKey(Users, on_delete=models.CASCADE)
    condition = models.CharField(
        max_length=2,
        choices=COND_CHOICES,
        default=NEW,
    )
    image = models.CharField(max_length=9999)

    # seller = models.CharField(max_length=255)


class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class Rating(models.Model):
    Grade = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), unique=True)
    Reviews = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)


class Bids(models.Model):
    Amount = models.IntegerField()
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
