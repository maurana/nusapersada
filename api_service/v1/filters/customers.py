from django_filters import rest_framework as filters
from v1.models.customers import Customers

class CustomersFilter(filters.FilterSet):
    customers_name = filters.CharFilter()

    class Meta:
        model = Customers
        fields = ['customers_name']