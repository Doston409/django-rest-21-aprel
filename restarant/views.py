from rest_framework.viewsets import ModelViewSet
from .models import Dish, Waiter, Table
from .serializers import DishSerializer, WaiterSerializer, TableSerializer


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class WaiterViewSet(ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer


class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer