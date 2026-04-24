from django.contrib import admin
from .models import Teacher,Student,Group
# Register your models here.



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name','ism_group_famiya','group','enrollment_date')
    search_fields = ('first_name','last_name')



