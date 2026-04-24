from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, BugReportViewSet, LaptopViewSet

router = DefaultRouter()
router.register(r'project', ProjectViewSet)
router.register(r'bugreport', BugReportViewSet)
router.register(r'laptop', LaptopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]