from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','grade','city','roll']
    list_display_links = ['id','name']
admin.site.register(Student, StudentAdmin)