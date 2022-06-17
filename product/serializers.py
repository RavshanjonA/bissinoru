from rest_framework.serializers import ModelSerializer

from product.models import Product, Order


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product.objects.all()
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order.objects.all()
        fields = "__all__"