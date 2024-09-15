from django.db import models
from v1.models.sales import Sales
from v1.models.products import Products

class Sale_Items(models.Model):
    item_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ITEM_ID')
    sales = models.ForeignKey(Sales, related_name='sales', on_delete=models.CASCADE)
    products = models.ForeignKey(Products, related_name='products', on_delete=models.CASCADE)
    item_price = models.FloatField(null=True, blank=True)
    item_qty = models.IntegerField(db_default=0)
    is_verify = models.IntegerField(db_default=0)
    
    class Meta:
        ordering = ['-item_id']