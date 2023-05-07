# Generated by Django 4.1.4 on 2023-04-30 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_product_offer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.offer'),
        ),
        migrations.AddField(
            model_name='offer',
            name='type',
            field=models.CharField(blank=True, choices=[('Product', 'Product'), ('Category', 'Category')], max_length=100, null=True),
        ),
    ]
