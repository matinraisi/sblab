from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    teacher = Teacher.objects.all()     
    
    context = {
        'teacher': teacher
    }    
    return render(request , 'home/index.html' , context)
def Courses(request):
    pass

def CourseDetails(request):
    return render(request , 'home/course-details.html')


def arezeyabi(request):
    return render(request , 'home/arezeyabi.html')