# Generated by Django 2.2.4 on 2019-08-07 14:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bought',
            field=models.ManyToManyField(blank=True, related_name='bought_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='cart',
            field=models.ManyToManyField(blank=True, related_name='cart_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='score',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
        ),
    ]
