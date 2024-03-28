from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'barcode', 'price')
    search_fields = ('name', 'barcode')
    list_filter = ('price',)
    list_per_page = 10
admin.site.register(Product, ProductAdmin)