# Generated by Django 4.1.7 on 2024-07-02 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image_product_stripe_price_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattachment',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
