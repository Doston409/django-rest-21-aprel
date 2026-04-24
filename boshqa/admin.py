from django.contrib import admin
from .models import HotelRoom,Employee,Movie
# Register your models here.

admin.site.register(HotelRoom)
admin.site.register(Employee)
admin.site.register(Movie)