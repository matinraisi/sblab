from django.db import models
from django_resized import ResizedImageField

class Teacher(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    rate = models.IntegerField(default=2)
    role = models.CharField(max_length=150)
    image = ResizedImageField(upload_to='images/Teacher', size=[120, 120], quality=75)

    def __str__(self):
        return self.name

class Course(models.Model):
    class Certificate(models.TextChoices):
        YES = 'Y', 'YES'
        NO = 'N', 'NO'

    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_capacity = models.IntegerField(default=5)
    certificate = models.CharField(max_length=1, choices=Certificate.choices)
    image_course = models.ImageField(upload_to="images/Course")
    description = models.TextField()

    def __str__(self):
        return self.title
class CourseSyllabus(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time_period = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class CourseSyllabusName(models.Model):
    syllabus = models.ForeignKey(CourseSyllabus, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)