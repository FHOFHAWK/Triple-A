from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


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

@receiver(post_save, sender=User)
def create_person_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_person(sender, instance, **kwargs):
    instance.person.save()

class Lesson(models.Model):
    title = models.CharField(max_length=512)
    groups = models.ManyToManyField(Role)
    teachers = models.ManyToManyField(Person)
    groups = models.ManyToManyField(StudyGroup)
    utlLesson = models.URLField()
    startTime = models.TimeField()
    endTime = models.TimeField()
