from django.urls import path 
from .views import *
appname = "home"
urlpatterns = [
    path('', index ),
    path('courses/', Courses , name = "Courses" ),
    path('course-details/', CourseDetails ),
    path('arezeyabi/', arezeyabi ),


]