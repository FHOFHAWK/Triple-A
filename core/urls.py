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
    path('sign_out/', views.sigh_out, name="sigh_out"),
    path('profile/', views.profile, name='profile'),
    path('add_teacher_to_lesson/', views.list_lessons_for_choose_teacher, name="list_lessons_for_choose_teacher"),
    path('add_teacher_to_lesson/<int:lesson_id>', views.add_teacher_to_lesson, name="add_teacher_to_lesson"),
    path('post_teacher_to_lesson/<int:teacher_id>/<int:lesson_id>', views.post_teacher_to_lesson, name="post_teacher_to_lesson"),
    path('accounts/', include('django.contrib.auth.urls')),

    path('get_finished_lessons', views.get_finished_lessons, name="get_finished_lessons")
]
