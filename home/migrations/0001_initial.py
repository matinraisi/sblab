# Generated by Django 5.1 on 2024-08-20 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('rate', models.IntegerField(default=2)),
                ('role', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/Teacher')),
            ],
        ),
    ]
