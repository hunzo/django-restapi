from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Items
from .serializers import ItemSerializers


@api_view(["GET"])
def getData(request):
    item = Items.objects.all()
    serializer = ItemSerializers(item, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def addData(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status=400)
    return Response(serializer.data)
