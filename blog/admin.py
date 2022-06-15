from django.contrib import admin

from blog.models import Item, OrderItem

admin.site.register(Item)
admin.site.register(OrderItem)
