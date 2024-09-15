from django.http import Http404
from django_filters import rest_framework as filters
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from v1.filters.customers import CustomersFilter
from v1.models.customers import Customers
from v1.serializers.customers import CustomersSerializer

class CustomersList(generics.ListCreateAPIView):
    serializer_class = CustomersSerializer
    filter_backends = ( filters.DjangoFilterBackend,)
    filterset_class = CustomersFilter

    def get_queryset(self):
        ids = self.request.query_params.get('ids', None)
        if ids is not None:
            ids = [ int(x) for x in ids.split(',') ]
            queryset = Customers.objects.filter(pk__in=ids)
        else:
            queryset = Customers.objects.all()

        return queryset
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = CustomersSerializer(queryset, many=True)
        response = {
            "ids": Customers.objects.values_list("customers_id", flat=True).order_by("customers_id"),
            "keyword": "",
            "total": Customers.objects.all().count(),
            "status": status.HTTP_200_OK,
            "rows": serializer.data
        }
        return Response(response)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomersDetail(APIView):

    # get object
    def get_object(self, pk):
        try:
            return Customers.objects.get(pk=pk)
        except Customers.DoesNotExist:
            raise Http404

    # get one
    def get(self, request, pk, format=None):
        customers = self.get_object(pk)
        serializer = CustomersSerializer(customers)
        return Response(serializer.data)

    # update
    def put(self, request, pk, format=None):
        customers = self.get_object(pk)
        serializer = CustomersSerializer(customers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # remove
    def delete(self, request, pk, format=None):
        customers = self.get_object(pk)
        customers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)