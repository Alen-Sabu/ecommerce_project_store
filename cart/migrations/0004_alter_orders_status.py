# Generated by Django 4.1.4 on 2023-04-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_orders_billing_address_shippingaddress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out For Shipping', 'Out For Shipping'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=150),
        ),
    ]