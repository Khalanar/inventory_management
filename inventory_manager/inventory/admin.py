from django.contrib import admin
from .models import Status, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'status',
        'stock',
        'price',
        'description',
    )

class StatusAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Status, StatusAdmin)