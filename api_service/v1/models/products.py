from django.db import models

class Products(models.Model):
    products_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='PRODUCTS_ID')
    products_name = models.CharField(max_length=250)
    products_code = models.CharField(max_length=15)
    products_price = models.FloatField(null=True, blank=True)
    products_stock = models.IntegerField(db_default=0)
    products_status = models.CharField(max_length=11, db_default='0')

    class Meta:
        ordering = ['-products_id']