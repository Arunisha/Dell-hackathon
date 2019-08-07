# Generated by Django 2.2.4 on 2019-08-04 05:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landing', '0005_auto_20190804_0446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bought',
        ),
        migrations.AddField(
            model_name='product',
            name='bought',
            field=models.ManyToManyField(related_name='bought_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='product',
            name='cart',
        ),
        migrations.AddField(
            model_name='product',
            name='cart',
            field=models.ManyToManyField(related_name='cart_set', to=settings.AUTH_USER_MODEL),
        ),
    ]