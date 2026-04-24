from rest_framework.viewsets import ModelViewSet
from .models import Apartment, Building, Land
from .serializers import ApartmentSerializer, BuildingSerializer, LandSerializer


class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class BuildingViewSet(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class LandViewSet(ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer