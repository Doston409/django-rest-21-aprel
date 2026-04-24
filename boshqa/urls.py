from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelRoomViewSet, EmployeeViewSet, MovieViewSet

router = DefaultRouter()
router.register(r'hotelroom', HotelRoomViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'movie', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]