from datetime import datetime, date, timedelta
from django.http import Http404
from django.db import transaction
from django.core.paginator import Paginator
from django.db.models import Q, OuterRef, Subquery, Sum, Count
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from v1.models.sales import Sales
from v1.models.products import Products
from v1.models.customers import Customers
from v1.models.sale_items import Sale_Items
from v1.serializers.sales import SalesSerializer
from v1.serializers.products import ProductsSerializer
from v1.serializers.sale_items import Sale_ItemsSerializer

class SalesList(APIView):
    def post(self, request):
        params = request.data["params"][0]
        queryset = Sales.objects.values('customers_id','sales_code','sales_date', 'sale_items_total', 'sale_price_total').annotate(customers_name=Subquery(Customers.objects.filter(customers_id=OuterRef('customers_id')).order_by('customers_id').values('customers_name')[:1])).filter(Q(sales_code__contains=params["keyword"]) | Q(customers_name__contains=params["keyword"]))
        if params["data_periode_start"] != "" and params["data_periode_end"] != "":
            date_start = datetime.strptime(params["data_periode_start"],'%d/%m/%Y').strftime('%Y-%m-%d')
            date_end = datetime.strptime(params["data_periode_end"],'%d/%m/%Y').strftime('%Y-%m-%d')
            queryset = Sales.objects.values('customers_id','sales_code','sales_date', 'sale_items_total', 'sale_price_total').annotate(customers_name=Subquery(Customers.objects.filter(customers_id=OuterRef('customers_id')).order_by('customers_id').values('customers_name')[:1])).filter(Q(sales_code__contains=params["keyword"]) | Q(customers_name__contains=params["keyword"])).filter(sales_date__range=[date_start, date_end])
            
        pg = Paginator(queryset, params["total_data_show"], allow_empty_first_page=True)
        page_number = request.GET.get("page")
        page_obj = pg.page(page_number)
        response = {
            "params": params,
            "data": [
                {
                    "keyword": params["keyword"],
                    "links": {
                        "start": page_obj.start_index(),
                        "next": page_obj.end_index(),
                    },
                    "total_data": page_obj.paginator.count,
                    "total_data_show": params["total_data_show"],
                    "total_page": page_obj.paginator.num_pages,
                    "has_next": page_obj.has_next(),
                    "has_previous": page_obj.has_previous(),
                    "Page": page_obj.number,
                    "status": status.HTTP_200_OK,
                    "rows": list(page_obj.object_list),
                }
            ]
        }
        return Response(response)

class SalesCreate(APIView):
    @transaction.non_atomic_requests
    def post(self, request, format=None):
        failed_si = 0
        saleitems = request.data["sale_items"]
        total_si = len(saleitems)
        serializer = SalesSerializer(data=request.data)
        with transaction.atomic():
            if serializer.is_valid():
                serializer.save()
                for i in range(len(saleitems)):
                    products = Products.objects.get(pk=saleitems[i]["products"])
                    p_serializer = ProductsSerializer(products)
                    saleitems[i]["sales"] = serializer.data["sales_id"]
                    if saleitems[i]["item_qty"] > p_serializer.data["products_stock"]:
                        failed_si = failed_si + 1
                        saleitems[i]["status"] =  "Failed - not enough Stock"
                    else:
                        saleitems[i]["status"] =  "Success"
                        newstock = p_serializer.data["products_stock"] - saleitems[i]["item_qty"]
                        si_serializer = Sale_ItemsSerializer(data=saleitems[i])
                        if si_serializer.is_valid():
                            si_serializer.save()
                            products.products_stock = int(newstock)
                            products.save()
                si = Sale_Items.objects.filter(sales=serializer.data["sales_id"]).values()
                totalprice = sum(map(float, [x * y for x, y in zip(si.values_list('item_price', flat=True), si.values_list('item_qty', flat=True))]))
                sales = Sales.objects.get(pk=serializer.data["sales_id"])
                sales.sale_items_total = int(total_si-failed_si)
                sales.sale_price_total = totalprice
                sales.save()
                response = {
                    "code": status.HTTP_200_OK,
                    "message": [
                        {
                          "total_items": total_si,
                          "total_sucess": total_si-failed_si,
                          "total_falied": failed_si
                        }
                    ],
                    "sale_items": saleitems
                }
                return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalesChart(APIView):
    def post(self, request, format=None):
        sales,items,prices,arr_date  = [],[],[],[]
        params = request.data["params"][0]
        dates = params["dates"]
        for i in range(0, len(dates)):
            arr_date.append(dates[i]["date"])
            sales.append(Sales.objects.filter(sales_date=dates[i]["date"]).count())
            items.append(list(Sales.objects.filter(sales_date=dates[i]["date"]).aggregate(Sum("sale_items_total")).values())[0])
            prices.append(list(Sales.objects.filter(sales_date=dates[i]["date"]).aggregate(Sum("sale_price_total")).values())[0])
        
        percentage = (len([ele for ele in prices if ele > 0]) / len(prices)) * 100
        amount = Sales.objects.filter(sales_date__in=arr_date).aggregate(Sum("sale_price_total")).values()
        response = {
            "sales": sales,
            "items": items,
            "prices": prices,
            "percentage": percentage,
            "categories": arr_date,
            "amount": list(amount)[0]
        }
        
        return Response(response)

class SalesDetail(APIView):

    # get object
    def get_object(self, pk):
        try:
            return Sales.objects.get(pk=pk)
        except Sales.DoesNotExist:
            raise Http404

    # get one
    def get(self, request, pk, format=None):
        sales = self.get_object(pk)
        serializer = SalesSerializer(sales)
        return Response(serializer.data)

    # update
    def put(self, request, pk, format=None):
        sales = self.get_object(pk)
        serializer = SalesSerializer(sales, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # remove
    def delete(self, request, pk, format=None):
        sales = self.get_object(pk)
        sales.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

