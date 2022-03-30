from rest_framework.viewsets import ModelViewSet

from stock.models import Stock
from stock.serializers import NewStockSerializer


class NewStockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = NewStockSerializer


