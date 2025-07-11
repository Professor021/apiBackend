# Generated by Django 5.2.4 on 2025-07-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_product_stock_product_in_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='product',
            name='review',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
