from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MotorcycleViewSet,SparePartViewSet,AutoServiceViewSet

router = DefaultRouter()
router.register(r'motorcycles', MotorcycleViewSet)
router.register(r'spareparts', SparePartViewSet)
router.register(r'autoservices', AutoServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]