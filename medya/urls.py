from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, BookViewSet, ExhibitionViewSet, PodcastViewSet

router = DefaultRouter()
router.register(r'song', SongViewSet)
router.register(r'book', BookViewSet)
router.register(r'exhibition', ExhibitionViewSet)
router.register(r'podcast', PodcastViewSet)

urlpatterns = [
    path('', include(router.urls)),
]