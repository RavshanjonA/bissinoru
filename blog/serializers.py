from cgi import FieldStorage
from rest_framework import serializers
from .models import Item, OrderItem


class ItemSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')


    def get_image_url(self,obj):
        return obj.image.url

    class Meta:
        model = Item
        fields = ["type","image", "image_url", "title", "size", "cost", "desctiption"]


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"