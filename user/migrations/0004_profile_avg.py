# Generated by Django 4.0.4 on 2022-05-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avg',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]