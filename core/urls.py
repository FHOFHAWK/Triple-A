from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login-user/', views.login_u, name='login-user'),
    path('recovery-password/', views.recovery_password, name='recovery-password'),
    path('lessons/', views.get_lessons, name="lessons"),
    # path('delete_lesson/', views.delete_lesson,name="delete_lesson")
    url(r'delete_lesson/(?P<pk>[0-9]+)/$', views.delete_lesson, name='delete_lesson'),
    path('filter/', views.filter_lessons, name="filter"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sign_out/', views.sigh_out, name="sigh_out")
]
