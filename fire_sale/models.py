from django.conf.global_settings import AUTH_USER_MODEL
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=9999)

    def __str__(self):
        return self.name


class Product(models.Model):
    NEW = 'NEW'
    PREOWNED = 'Pre Owned'
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
        max_length=20,
        choices=COND_CHOICES,
        default=NEW,
    )
    image = models.CharField(max_length=9999)
    seller = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    payment = models.BooleanField(default=False)


class ProductImage(models.Model):
    image = models.CharField(max_length=9999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class Rating(models.Model):
    Grade = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])
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
    Country = CountryField()  # Gera select html element
    Zip = models.IntegerField()


def credit_card_check(num):
    if len(str(int(num))) != 16:
        raise ValidationError('Card number needs to be 16 nums')


def check_exp_year(num):
    if len(str(int(num))) != 4:
        raise ValidationError('year has to be 4 letter long')


def check_cvc(num):
    if len(str(int(num))) != 3:
        raise ValidationError('cvc must be 3 letters long')


class PaymentInformation(models.Model):
    Name_of_cardholder = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
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
    Exp_month = models.CharField(
        max_length=2,
        choices=MONTH_CHOICES,
        default=JAN,
    )
    Exp_year = models.IntegerField(
        validators=[
            check_exp_year
        ]
    )
    CVC = models.IntegerField(
        validators=[
            check_cvc
        ]
    )


class Notification(models.Model):

    seen = models.BooleanField(default=False)
    message = models.CharField(max_length=255)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
