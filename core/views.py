from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from core.models import Lesson, User, Teacher, Student
from django.shortcuts import redirect, render

from utils.constants import teacher, student
from utils.helpers import check_if_teacher
from .forms import CreateLessonForm, FilterLessonForm, CreateUserForm, LoginForm


def main(request):
    return render(request, 'main.html')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            patronymic = form.cleaned_data.get("patronymic")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            password_repeat = form.cleaned_data.get("password_repeat")
            role = form.cleaned_data.get("role")

            if password == password_repeat:
                if role == teacher:
                    teacher_obj = Teacher.objects.create(username=username,
                                                         first_name=first_name,
                                                         last_name=last_name,
                                                         patronymic=patronymic,
                                                         email=email,
                                                         password=password,
                                                         role=role)
                    teacher_obj.save()
                    return redirect("/login-user")
                elif role == student:
                    teacher_obj = Student.objects.create(username=username,
                                                         first_name=first_name,
                                                         last_name=last_name,
                                                         patronymic=patronymic,
                                                         email=email,
                                                         password=password,
                                                         role=role)
                    teacher_obj.save()
                    return redirect("/login-user")
    return render(request, "register.html", {"form": form})


def login_u(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user_from_db = User.objects.filter(email=email)
            if password == (user_from_db[0]).password:
                if user_from_db:
                    login(request, user_from_db[0])
                    return redirect('/lessons')

    return render(request, "login.html", {"form": form})


def recovery_password(request):
    return render(request, 'recovery-password.html')


@login_required
def get_lessons(request):
    if user := check_if_teacher(user=request.user):
        teacher_lessons = Lesson.objects.filter(teachers=user)
        return render(request, "teacher_lessons.html", {"teacher_lessons": teacher_lessons})
    form = CreateLessonForm()
    if request.method == "GET":
        lessons = Lesson.objects.all()
        return render(request, "lesson.html", {"form": form, "lessons": lessons})
    elif request.method == "POST":
        form = CreateLessonForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            end_time = form.cleaned_data.get("end_time")
            start_time = form.cleaned_data.get("start_time")
            url_lesson = form.cleaned_data.get("url_lesson")
            lesson = Lesson.objects.create(title=title, end_time=end_time, start_time=start_time, url_lesson=url_lesson)
            lesson.save()
    lessons = Lesson.objects.all()
    return render(request, "lesson.html", {"form": form, "lessons": lessons})


def delete_lesson(request, pk):
    if request.method == "POST":
        lesson = Lesson.objects.filter(id=int(pk))
        lesson.delete()
    lessons = Lesson.objects.all()
    form = CreateLessonForm(request.POST)
    return redirect('/lessons')


def filter_lessons(request):
    form = FilterLessonForm()
    if request.method == "GET":
        lessons = Lesson.objects.all()
        return render(request, "filter.html", {"form": form, "lessons": lessons})
    elif request.method == "POST":
        form = FilterLessonForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            end_time = form.cleaned_data.get("end_time")
            start_time = form.cleaned_data.get("start_time")
            url_lesson = form.cleaned_data.get("url_lesson")
            lessons = Lesson.objects.all()
            if title:
                lessons = Lesson.objects.all().filter(title=title)
            # if group:
            #   lessons = Lesson.objects.all().filter(group=group)
            # if teacher:
            #   lessons = Lesson.objects.all().filter(teacher=teacher)

            return render(request, "filter.html", {"form": form, "lessons": lessons})
