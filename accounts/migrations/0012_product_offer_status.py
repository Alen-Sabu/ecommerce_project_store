# Generated by Django 4.1.4 on 2023-04-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_product_offer_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer_status',
            field=models.BooleanField(default=False),
        ),
    ]
