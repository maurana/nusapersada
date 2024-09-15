from django_filters import rest_framework as filters
from v1.models.sales import Sales

class SalesFilter(filters.FilterSet):
    sales_code = filters.CharFilter()
    customers_name = filters.CharFilter()

    class Meta:
        model = Sales
        fields = "__all__"