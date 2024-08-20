from django.contrib import admin
from .models import *

class CourseSyllabusInline(admin.TabularInline):
    model = CourseSyllabus
    extra = 1

class CourseSyllabusNameInline(admin.TabularInline):
    model = CourseSyllabusName
    extra = 5

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display  = ['name' , 'role' , 'rate' ,]
    ordering = ['name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display  = ['title' , 'price']
    ordering = ['title']
    inlines = [CourseSyllabusInline]

@admin.register(CourseSyllabus)
class CourseSyllabusAdmin(admin.ModelAdmin):
    list_display  = ['course' ,]
    inlines = [CourseSyllabusNameInline]

@admin.register(CourseSyllabusName)
class CourseSyllabusNameAdmin(admin.ModelAdmin):
    list_display  = ['title']