from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, DriverViewSet, RouteViewSet

router = DefaultRouter()
router.register(r'car', CarViewSet)
router.register(r'driver', DriverViewSet)
router.register(r'route', RouteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]