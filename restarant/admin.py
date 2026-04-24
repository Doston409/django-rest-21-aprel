from django.contrib import admin
from .models import Dish,Waiter,Table
# Register your models here.

admin.site.register(Dish)
admin.site.register(Waiter)
admin.site.register(Table)
