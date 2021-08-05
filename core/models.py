from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _


class StudyGroup(models.Model):
    group_title = models.CharField(max_length=15)


class User(AbstractUser):
    class Role(models.TextChoices):
        TEACHER = "Teacher", _("Teacher")
        STUDENT = "Student", _("Student")
        ADMIN = "Admin", _("Admin")

    patronymic = models.CharField(max_length=40)
    role = models.CharField(choices=Role.choices,
                            default=Role.STUDENT,
                            max_length=7)


class Subject(models.Model):
    title = models.CharField(max_length=100, default='default title')


class Student(User):
    group = models.ForeignKey(StudyGroup,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True)


class Teacher(User):
    count_of_lessons = models.IntegerField(default=0)
    count_of_completed_lessons = models.IntegerField(default=0)
    teaching_subjects = models.ManyToManyField(Subject)
    teaching_students = models.ManyToManyField(Student)


class Lesson(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    teachers = models.ManyToManyField(Teacher)
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
