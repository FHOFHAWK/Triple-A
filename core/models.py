from django.db import models
from django.contrib.auth.models import AbstractUser

class StudyGroup(models.Model):
    group_title = models.CharField(max_length=15)


class User(AbstractUser):
    patronymic = models.CharField(max_length=40)
    role = models.CharField(max_length=40)
    # group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, null=True, blank=True)

class Role(models.Model):
    TEACHER = 1
    STUDENT = 2
    ROLE_CHOICES = (
          (TEACHER, 'Teacher'),
          (STUDENT, 'Student'),
      )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)


class Subject(models.Model):
    title = models.CharField(max_length=100,default='default title')

class Student(User):
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)

class Teacher(User):
    count_of_lessons = models.IntegerField()
    count_of_completed_lessons = models.IntegerField()
    teaching_subjets = models.ManyToManyField(Subject)
    teaching_students = models.ManyToManyField(Student)

class Lesson(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=100)
    # teachers = models.ManyToManyField(Person)
    # groups = models.ManyToManyField(StudyGroup)
    url_lesson = models.URLField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class HasedVides(models.Model):
    hash = models.BinaryField()

class FilterLesson(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    # teachers = models.ManyToManyField(Person)
    # groups = models.ManyToManyField(StudyGroup)
    url_lesson = models.URLField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
