# Generated by Django 3.0.5 on 2020-04-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default=1212, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='oldprice',
            field=models.CharField(default=12, max_length=10),
            preserve_default=False,
        ),
    ]
