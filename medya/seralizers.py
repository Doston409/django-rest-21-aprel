from rest_framework import serializers
from .models import Song, Book, Exhibition, Podcast


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'
        