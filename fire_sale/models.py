from django.conf.global_settings import AUTH_USER_MODEL
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


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
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )

    condition = models.CharField(
        max_length=2,
        choices=COND_CHOICES,
        default=NEW,
    )
    image = models.CharField(max_length=9999)
    seller = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)


class ProductImage(models.Model):
    image = models.CharField(max_length=9999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class Rating(models.Model):
    Grade = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), unique=True)
    Reviews = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Bids(models.Model):
    Amount = models.IntegerField()
    Bid_user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ContactInformation(models.Model):
    Full_name = models.CharField(max_length=255)
    Street_name = models.CharField(max_length=255)
    House_number = models.IntegerField()
    City = models.CharField(max_length=255)
    Country = models.CharField(max_length=255) # Gera select html element
    Zip = models.IntegerField(
        validators=[
            MaxValueValidator(10)
        ]
    )


class PaymentInformation(models.Model):
    JAN = '01'
    FEB = '02'
    MAR = '03'
    APR = '04'
    MAY = '05'
    JUN = '06'
    JUL = '07'
    AUG = '08'
    SEP = '09'
    OKT = '10'
    NOV = '11'
    DEC = '12'
    MONTH_CHOICES = [
        (JAN, 'JAN'),
        (FEB, 'FEB'),
        (MAR, 'MAR'),
        (APR, 'APR'),
        (MAY, 'MAY'),
        (JUN, 'JUN'),
        (JUL, 'JUL'),
        (AUG, 'AUG'),
        (SEP, 'SEP'),
        (OKT, 'OKT'),
        (NOV, 'NOV'),
        (DEC, 'DEC'),
    ]
    Name_of_cardholder = models.CharField(max_length=255)
    card_number = models.IntegerField(
        validators=[
            MaxValueValidator(16)
        ]
    )
    Exp_month = models.CharField(
        max_length=2,
        choices=MONTH_CHOICES,
        default=JAN,
    )
    Exp_year = models.IntegerField(
        validators=[
            MaxValueValidator(4)
        ]
    )
    CVC = models.IntegerField(
        validators=[
            MinValueValidator(3),
            MaxValueValidator(3)
        ]
    )
