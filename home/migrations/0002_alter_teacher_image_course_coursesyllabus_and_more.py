# Generated by Django 5.1 on 2024-08-20 08:35

import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, scale=None, size=[120, 120], upload_to='images/Teacher'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('course_capacity', models.IntegerField(default=5)),
                ('certificate', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=1)),
                ('image_course', models.ImageField(upload_to='images/Course')),
                ('description', models.TextField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSyllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_period', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSyllabusName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('syllabus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.coursesyllabus')),
            ],
        ),
    ]
