# Generated by Django 2.2.4 on 2019-08-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shipping_cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
