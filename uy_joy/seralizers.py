from rest_framework import serializers
from .models import Apartment, Building, Land


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'