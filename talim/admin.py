from django.contrib import admin
from .models import Group,Course,Subject,Grade,LibraryCard
# Register your models here.

admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(LibraryCard)