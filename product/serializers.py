from rest_framework.serializers import ModelSerializer

from product.models import Product, Order
from product.templates.bot import order_product_on_telegram


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        order_product_on_telegram(validated_data)
        return super().create(validated_data)
