# Generated by Django 4.0.4 on 2022-05-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fire_sale', '0043_alter_contactinformation_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=999),
        ),
    ]