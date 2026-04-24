from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AthleteViewSet, GymViewSet, CompetitionViewSet, CoachViewSet

router = DefaultRouter()
router.register(r'athlete', AthleteViewSet)
router.register(r'gym', GymViewSet)
router.register(r'competition', CompetitionViewSet)
router.register(r'coach', CoachViewSet)

urlpatterns = [
    path('', include(router.urls)),
]