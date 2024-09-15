from datetime import date, timedelta
from django.http import Http404
from django.db.models import Q, OuterRef, Subquery
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from v1.models.products import Products
from v1.serializers.products import ProductsSerializer

class ProductsList(APIView):

    # list all
    def get(self, request, format=None):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    # create
    def post(self, request, format=None):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductsPopular(APIView):
    def post(self, request, format=None):
        data = []
        set_limit = 5
        date_end = date.today()
        date_start = date_end - timedelta(7)
        params = request.data["params"][0]
        if params["total_data_show"] != 0:
            set_limit = params["total_data_show"]
        if params["data_periode_start"] != "":
            date_start = params["data_periode_start"]
        if params["data_periode_end"] != "":
            date_end = params["data_periode_end"]
        querystr = "SELECT v1_products.products_id, v1_products.products_name, v1_products.products_price, SUM(v1_sale_items.item_qty) AS total_qty, SUM(v1_sale_items.item_price) AS total_price FROM v1_sale_items INNER JOIN v1_products ON v1_sale_items.products_id = v1_products.products_id INNER JOIN v1_sales ON v1_sale_items.sales_id = v1_sales.sales_id WHERE v1_sales.sales_date BETWEEN '" + str(date_start) + "' AND '" + str(date_end) +"' GROUP BY v1_products.products_id ORDER BY SUM(v1_sale_items.item_price) DESC LIMIT " + str(set_limit)
        queryset = Products.objects.raw(querystr)
        for p in queryset:
            data.append({"products_id": p.products_id,"products_name": p.products_name,"products_price": p.products_price,"total_qty": p.total_qty,"total_price": p.total_price})
        return Response({"params": params, "data": data})

class ProductsDetail(APIView):

    # get object
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    # get one
    def get(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ProductsSerializer(products)
        message = ""
        if serializer.data['products_stock'] == 0:
            message = "Stock is 0"
        if serializer.data['products_status'] == "Hold":
            message = "Status is Hold"
        if serializer.data['products_status'] == "Hold" and serializer.data['products_stock'] == 0:
            message = "Status is Hold & Stock is 0"
        response = {
            "code": serializer.data['products_code'],
            "status": status.HTTP_200_OK,
            "message": message,
            "data": serializer.data
        }
        return Response(response)

    # update
    def put(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ProductsSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # remove
    def delete(self, request, pk, format=None):
        products = self.get_object(pk)
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)