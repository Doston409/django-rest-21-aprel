from rest_framework import serializers
from .models import Athlete, Gym, Competition, Coach


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'
        