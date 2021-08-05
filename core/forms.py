from django import forms
from django.forms import ModelForm
from .models import Lesson, FilterLesson, User


class CreateLessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ["title", "start_time","end_time", "url_lesson"]


class FilterLessonForm(ModelForm):
    class Meta:
        model = FilterLesson
        fields = ["title", "start_time","end_time", "url_lesson"]


class CreateUserForm(ModelForm):
    password_repeat = forms.CharField(max_length=100, help_text='Повтор пароля')

    class Meta:
        model = User
        fields = ["first_name", "last_name", "patronymic", "email", "password", "password_repeat", "role"]


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]
