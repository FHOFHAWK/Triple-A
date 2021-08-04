# from django.contrib.auth.models import User, Group
# from django.http import HttpResponse
# from rest_framework import serializers, viewsets
# from rest_framework import permissions
# from core.serializers import UserSerializer, GroupSerializer, RegistrationSerializer
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# @api_view(['POST'])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             person = serializer.save()
#             data['response'] = "succsessfully registered user"
#             data['email'] = person.email
#         else:
#             data = serializer.errors
#         return Response(data)
#
#
# def register(request):
#     if request.method == "GET":
#         return HttpResponse("index.")
#
#     return HttpResponse("Hello, world. You're at the polls index.")
from django import forms
from django.http.response import HttpResponse
from core.models import Lesson
from django.shortcuts import redirect, render
from .forms import CreateLessonForm


def main(request):
    return render(request, 'main.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def recovery_password(request):
    return render(request, 'recovery-password.html')

def get_lessons(request):
    form = CreateLessonForm()
    if request.method == "GET":
        lessons = Lesson.objects.all()
        return render(request,"lesson.html",{"form" : form, "lessons" : lessons})
    elif request.method == "POST":
        form = CreateLessonForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            end_time = form.cleaned_data.get("end_time")
            start_time = form.cleaned_data.get("start_time")
            url_lesson = form.cleaned_data.get("url_lesson")
            lesson = Lesson.objects.create(title=title,end_time=end_time,start_time=start_time,url_lesson=url_lesson)
            lesson.save()
    lessons = Lesson.objects.all()
    return render(request,"lesson.html",{"form" : form, "lessons" : lessons})

def delete_lesson(request,pk):
    print(request)
    print(pk)
    if request.method == "POST":
        lesson = Lesson.objects.filter(id=int(pk))
        lesson.delete()
    lessons = Lesson.objects.all()
    form = CreateLessonForm(request.POST)
    return redirect('/lessons')