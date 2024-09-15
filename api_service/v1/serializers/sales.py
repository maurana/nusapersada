from rest_framework import serializers
from v1.models.sales import Sales

class SalesSerializer(serializers.ModelSerializer):
    # sales_date = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601'])
    class Meta:
        model = Sales
        fields = '__all__'