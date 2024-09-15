from django.db import models

class Customers(models.Model):
    customers_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='CUSTOMERS_ID')
    customers_name = models.CharField(max_length=100)

    # def __str__(self):
    #     return '%d: %s' % (self.customers_id , self.customers_name)
    
    def __str__(self):
        return self.customers_name

    class Meta:
        ordering = ['-customers_id']