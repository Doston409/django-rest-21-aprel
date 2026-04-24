from rest_framework.viewsets import ModelViewSet
from .models import Athlete, Gym, Competition, Coach
from .serializers import AthleteSerializer, GymSerializer, CompetitionSerializer, CoachSerializer


class AthleteViewSet(ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer


class GymViewSet(ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


class CompetitionViewSet(ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CoachViewSet(ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer