from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.serializers import ItemSerializer
from .models import Item
from rest_framework.views import APIView


class ItemViewSet(APIView):

    # def post(self, request, *args, **kwargs):
    #     file = request.data['file']
    #     image = Item.objects.create(image=file)
    #     return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

    def get(self, request, *args, **kwargs):
        items = Item.objects.all()
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data)
