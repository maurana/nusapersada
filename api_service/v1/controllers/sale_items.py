from django.http import Http404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from v1.models.sales import Sales
from v1.models.sale_items import Sale_Items
from v1.serializers.sale_items import Sale_ItemsSerializer

class Sale_ItemsList(APIView):

    # list all
    def get(self, request, format=None):
        sale_items = Sale_Items.objects.all()
        serializer = Sale_ItemsSerializer(sale_items, many=True)
        return Response(serializer.data)

    # create
    def post(self, request, format=None):
        serializer = Sale_ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sale_ItemsDetail(APIView):

    # get object
    def get_object(self, pk):
        try:
            return Sale_Items.objects.get(pk=pk)
        except Sale_Items.DoesNotExist:
            raise Http404

    # get one
    def get(self, request, pk, format=None):
        sale_items = self.get_object(pk)
        serializer = Sale_ItemsSerializer(sale_items)
        return Response(serializer.data)

    # update
    def put(self, request, pk, format=None):
        sale_items = self.get_object(pk)
        serializer = Sale_ItemsSerializer(sale_items, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # remove
    def delete(self, request, pk, format=None):
        sale_items = self.get_object(pk)
        sales = Sales.objects.get(pk=sale_items.sale_id)
        sales.sale_items_total = int(sales.sale_items_total - 1)
        sale_items.delete()
        sales.save()
        return Response(status=status.HTTP_204_NO_CONTENT)