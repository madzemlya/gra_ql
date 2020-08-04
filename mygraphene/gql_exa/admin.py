from django.contrib import admin

from .models import School, Student, City


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'number'
    list_display_links = 'id',


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    list_display_links = 'id',


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    list_display_links = 'id',
