from django.contrib import admin
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'get_product_name', 'quantity', 'placed_at', 'status')
    list_filter = ('status',)
    search_fields = ('customer__username', 'product__product_name')  
    readonly_fields = ('placed_at',) 

    def get_product_name(self, obj):
        return obj.product.product_name
    get_product_name.short_description = 'Product Name'
admin.site.register(Order, OrderAdmin)
