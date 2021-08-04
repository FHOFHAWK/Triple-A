from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('recovery-password/', views.recovery_password, name='recovery-password'),
    path('lessons/',views.get_lessons,name="lessons")
]
