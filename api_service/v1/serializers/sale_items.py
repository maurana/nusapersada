from rest_framework import serializers
from v1.models.sale_items import Sale_Items

class Sale_ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale_Items
        fields = '__all__'