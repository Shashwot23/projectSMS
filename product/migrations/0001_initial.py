# Generated by Django 4.2.7 on 2024-02-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_image', models.ImageField(upload_to='product_images/')),
                ('product_description', models.TextField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_stock', models.PositiveIntegerField()),
            ],
        ),
    ]
