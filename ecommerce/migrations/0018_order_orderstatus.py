# Generated by Django 3.0.5 on 2020-05-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0017_billingaddress_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderstatus',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
