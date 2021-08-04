# from django.db import models
# from django import forms
# from django.contrib.auth.models import User, AbstractUser
# from django.dispatch import receiver
# from django.db.models.signals import post_save
#
#
# class StudyGroup(models.Model):
#     groupNumber = models.CharField(max_length=15)
#
#
# class Person(AbstractUser):
#     role = models.CharField(default="Пользователь", max_length=20)
#     group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, null=True, blank=True)
#
#
# class Lesson(models.Model):
#     title = models.CharField(max_length=100)
#     teachers = models.ManyToManyField(Person)
#     groups = models.ManyToManyField(StudyGroup)
#     utlLesson = models.URLField()
#     startTime = models.TimeField()
#     endTime = models.TimeField()
