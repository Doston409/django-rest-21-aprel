from rest_framework.viewsets import ModelViewSet
from .models import Car, Driver, Route
from .serializers import CarSerializer, DriverSerializer, RouteSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class RouteViewSet(ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer