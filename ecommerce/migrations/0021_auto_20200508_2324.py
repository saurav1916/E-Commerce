# Generated by Django 3.0.5 on 2020-05-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0020_auto_20200508_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderstatus',
            field=models.BooleanField(default=False),
        ),
    ]
