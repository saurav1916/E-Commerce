# Generated by Django 3.0.5 on 2020-05-06 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0014_billingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderaddress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.BillingAddress'),
        ),
    ]
