from rest_framework import serializers
from .models import Motorcycle, SparePart, AutoService


class MotorcycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = '__all__'


class SparePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SparePart
        fields = '__all__'


class AutoServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoService
        fields = '__all__'