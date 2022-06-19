from django.contrib import admin
from django.contrib.admin import ModelAdmin

from product.models import Product, Order

admin.site.site_header = 'Bssinuro Adminstration'
admin.site.index_title = 'Bssinuro area'
admin.site.site_title = 'Bssinuro'

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ["title", "price", "size"]


@admin.register(Order)
class ProductAdmin(ModelAdmin):
    list_display = ["username", "phone", "summa"]
