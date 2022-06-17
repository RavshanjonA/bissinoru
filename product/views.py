from rest_framework.views import APIView
from rest_framework.response import Response

from product.models import Product, Order
from product.serializers import ProductSerializer


class ProductAPIView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(data=serializer.data)


class OrderAPIView(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = ProductSerializer(orders, many=True)
        return Response(data=serializer.data)
