from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


class StudyGroup(models.Model):
    group_title = models.CharField(max_length=15)


class User(AbstractUser):
    patronymic = models.CharField(max_length=40)
    role = models.CharField(max_length=40)
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, null=True, blank=True)


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    # teachers = models.ManyToManyField(Person)
    # groups = models.ManyToManyField(StudyGroup)
    url_lesson = models.URLField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class FilterLesson(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    # teachers = models.ManyToManyField(Person)
    # groups = models.ManyToManyField(StudyGroup)
    url_lesson = models.URLField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
