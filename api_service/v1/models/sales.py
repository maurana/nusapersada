from django.db import models
from django.conf import settings
from v1.models.customers import Customers

class Sales(models.Model):
    sales_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='SALES_ID')
    customers = models.ForeignKey(Customers, related_name='customers', on_delete=models.CASCADE)
    sales_code = models.CharField(max_length=15)
    sales_date = models.DateField(null=True, blank=True)
    sale_items_total = models.IntegerField(db_default=0)
    sale_price_total = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['-sales_id']