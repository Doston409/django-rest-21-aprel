from django.contrib import admin
from .models import Athlete,Gym,Competition,Coach
# Register your models here.

admin.site.register(Athlete)
admin.site.register(Gym)
admin.site.register(Competition)
admin.site.register(Coach)
