# Generated by Django 3.0.5 on 2020-05-08 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0021_auto_20200508_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderaddress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.BillingAddress'),
        ),
    ]
