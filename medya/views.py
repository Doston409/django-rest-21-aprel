from rest_framework.viewsets import ModelViewSet
from .models import Song, Book, Exhibition, Podcast
from .serializers import SongSerializer, BookSerializer, ExhibitionSerializer, PodcastSerializer


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ExhibitionViewSet(ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer


class PodcastViewSet(ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer