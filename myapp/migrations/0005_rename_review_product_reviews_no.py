# Generated by Django 5.2.4 on 2025-07-11 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_product_discount_product_features_product_rating_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='review',
            new_name='reviews_no',
        ),
    ]
