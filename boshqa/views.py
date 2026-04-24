from rest_framework.viewsets import ModelViewSet
from .models import HotelRoom, Employee, Movie
from .serializers import HotelRoomSerializer, EmployeeSerializer, MovieSerializer


class HotelRoomViewSet(ModelViewSet):
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer