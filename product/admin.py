from django.contrib import admin
from product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=(
        'product_name',
        'product_image',
        'product_description',
        'product_price',
        'product_stock'
    )

admin.site.register(Product,ProductAdmin)