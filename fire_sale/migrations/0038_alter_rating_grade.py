# Generated by Django 4.0.4 on 2022-05-12 09:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fire_sale', '0037_remove_rating_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='Grade',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
