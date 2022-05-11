# Generated by Django 4.0.4 on 2022-05-11 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fire_sale', '0030_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=9999)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fire_sale.productcategory')),
            ],
        ),
    ]