from django.db import models
from autoslug import AutoSlugField

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='product_images/')
    product_description = models.TextField()
    product_price = models.PositiveIntegerField()
    product_stock = models.PositiveIntegerField()
    product_slug = AutoSlugField(populate_from='product_name', unique=True, null=True, default=None)

