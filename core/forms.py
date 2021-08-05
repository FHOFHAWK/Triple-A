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
        password = forms.CharField(widget=forms.PasswordInput)
        password_repeat = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
            'password_repeat' : forms.PasswordInput(),
        }
        fields = ["first_name", "last_name", "patronymic", "email", "password", "password_repeat", "role"]

class ProfileUserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "patronymic", "email"]


class LoginForm(ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
        }
        model = User
        fields = ["email", "password"]
