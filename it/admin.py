from django.contrib import admin
from .models import Project,BugReport,Laptop
# Register your models here.

admin.site.register(Project)
admin.site.register(BugReport)
admin.site.register(Laptop)