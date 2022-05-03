from django.db import models

# Create your models here.
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

class Rating(models.Model):
    Grade = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), unique=True)
    Reviews = models.CharField(max_length=255, blank=True)

class Bids(models.Model):
    Amount = models.IntegerField()
