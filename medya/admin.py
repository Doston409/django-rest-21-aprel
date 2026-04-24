from django.contrib import admin
from .models import Song,Book,Exhibition,Podcast
# Register your models here.


admin.site.register(Song)
admin.site.register(Book)
admin.site.register(Exhibition)
admin.site.register(Podcast)