# Generated by Django 3.0.5 on 2020-04-30 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]
