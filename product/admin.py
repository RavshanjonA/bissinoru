from django.contrib import admin
from django.contrib.admin import ModelAdmin

from product.models import Product, Order


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ["title", "price", "size"]


@admin.register(Order)
class ProductAdmin(ModelAdmin):
    list_display = ["username", "phone", "summa"]
