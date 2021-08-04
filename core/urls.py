from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('recovery-password/', views.recovery_password, name='recovery-password'),
    path('lessons/',views.get_lessons,name="lessons"),
    # path('delete_lesson/', views.delete_lesson,name="delete_lesson")
    url(r'delete_lesson/(?P<pk>[0-9]+)/$', views.delete_lesson, name='delete_lesson')
]
