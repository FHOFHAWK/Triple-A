from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Role(models.Model):
    TEACHER = 1
    STUDENT = 2
    ROLE_CHOICES = (
          (TEACHER, 'Teacher'),
          (STUDENT, 'Student'),
      )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

class StudyGroup(models.Model):
    groupNumber = models.CharField(max_length=15)

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE) 
    group = models.ForeignKey(StudyGroup,on_delete=models.CASCADE, null=True, blank=True)

class Lesson(models.Model):
    title = models.CharField(max_length=512)
    groups = models.ManyToManyField(Role)
    teachers = models.ManyToManyField(Person)
    groups = models.ManyToManyField(StudyGroup)
    utlLesson = models.URLField()
    startTime = models.TimeField()
    endTime = models.TimeField()
