from rest_framework.serializers import ModelSerializer
from stock.models import Stock


class NewStockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
