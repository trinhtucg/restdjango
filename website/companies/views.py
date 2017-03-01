from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from companies.models import Stock
from .serializers import StockSerializer


class StockAPI(APIView):

    def get(self, request):
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

class JSONResponse(HttpResponse):

    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def stock_list(request):
    """
    List all or create a new stock
    """
    if request.method == 'GET':
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        pass