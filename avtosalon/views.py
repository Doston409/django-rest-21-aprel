from rest_framework.viewsets import ModelViewSet
from .serializers import MotorcycleSerializer, SparePartSerializer, AutoServiceSerializer
from .models import Motorcycle, SparePart, AutoService


class MotorcycleViewSet(ModelViewSet):
    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer


class SparePartViewSet(ModelViewSet):
    queryset = SparePart.objects.all()
    serializer_class = SparePartSerializer


class AutoServiceViewSet(ModelViewSet):
    queryset = AutoService.objects.all()
    serializer_class = AutoServiceSerializer