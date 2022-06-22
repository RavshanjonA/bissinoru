from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product.models import Product, Order
from product.serializers import ProductSerializer, OrderSerializer


class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(data=serializer.data)
    # def post(self, request, *args, **kwargs):
    #     file = request.data['file']
    #     image = Product.objects.create(image=file)
    #     return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

class OrderAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
