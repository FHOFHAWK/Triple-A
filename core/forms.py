from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Lesson

class CreateLessonForm(ModelForm):

    class Meta:
	    model = Lesson
	    fields = ["end_time", "start_time", "url_lesson", "title"]