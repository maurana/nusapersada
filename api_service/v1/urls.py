from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from v1.controllers.customers import *
from v1.controllers.products import *
from v1.controllers.sales import *
from v1.controllers.sale_items import *
 
urlpatterns = [ 
    path('customers', CustomersList.as_view()),
    path('customers/<int:pk>', CustomersDetail.as_view()),
    path('products', ProductsList.as_view()),
    path('products/<int:pk>', ProductsDetail.as_view()),
    path('products_popular', ProductsPopular.as_view()),
    path('sales', SalesList.as_view()),
    path('sales_create', SalesCreate.as_view()),
    path('sales_chart', SalesChart.as_view()),
    path('sales/<int:pk>', SalesDetail.as_view()),
    path('sale_items', Sale_ItemsList.as_view()),
    path('sale_items/<int:pk>', Sale_ItemsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)