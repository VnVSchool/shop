# Generated by Django 4.2.1 on 2023-05-17 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_product_discount_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="show_on_main_page",
            field=models.BooleanField(default=False),
        ),
    ]
