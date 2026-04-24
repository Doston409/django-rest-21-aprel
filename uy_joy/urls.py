from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApartmentViewSet, BuildingViewSet, LandViewSet

router = DefaultRouter()
router.register(r'apartment', ApartmentViewSet)
router.register(r'building', BuildingViewSet)
router.register(r'land', LandViewSet)

urlpatterns = [
    path('', include(router.urls)),
]