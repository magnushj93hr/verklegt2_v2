# Generated by Django 4.0.4 on 2022-05-13 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fire_sale', '0047_alter_product_highest_bidder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='highest_bidder',
        ),
    ]