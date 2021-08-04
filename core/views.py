from django.contrib.auth.models import User, Group
from rest_framework import serializers, viewsets
from rest_framework import permissions
from core.serializers import UserSerializer, GroupSerializer, RegistrationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Lesson, StudyGroup
from django.contrib.auth.decorators import login_required


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            person = serializer.save()
            data['response'] = "succsessfully registered user"
            data['email'] = person.email
        else:
            data = serializer.errors
        return Response(data)


@login_required(login_url='/accounts/login/')
def index(request):
    lessons = Lesson.objects.all()

    return render(
        request,
        'index.html',
        context={'lessons': lessons},
    )
