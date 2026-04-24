from django.contrib import admin
from .models import Motorcycle, SparePart,AutoService
# Register your models here.


admin.site.register(Motorcycle)
admin.site.register(SparePart)
admin.site.register(AutoService)