from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from core.models import Lesson, StudyGroup, User, Teacher, Student
from django.shortcuts import redirect, render
from utils.constants import teacher, student, admin
from utils.helpers import check_if_teacher, admin_only, auth_user_only, teacher_and_admin_only
from utils.video_comparison import file_unique
from .forms import CreateLessonForm, FilterLessonForm, CreateUserForm, LoginForm, ProfileUserForm


def main(request):
    return render(request, 'main.html')


@login_required
def sigh_out(request):
    logout(request)
    return redirect('/login-user')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("email")
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
                elif role == student:
                    student_obj = Student(username=username,
                                          first_name=first_name,
                                          last_name=last_name,
                                          patronymic=patronymic,
                                          email=email,
                                          password=password,
                                          role=role
                                          )
                    student_obj.group.add(1)
                    student_obj.save()
                    return redirect("/login-user")
                elif role == admin:
                    admin_obj = User.objects.create(username=username,
                                                    first_name=first_name,
                                                    last_name=last_name,
                                                    patronymic=patronymic,
                                                    email=email,
                                                    password=password,
                                                    role=role)
                    admin_obj.save()
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
            if user_from_db and password == (user_from_db[0]).password:
                if user_from_db:
                    login(request, user_from_db[0])
                    return redirect('/lessons')

    return render(request, "login.html", {"form": form})


def recovery_password(request):
    return render(request, 'recovery-password.html')


@auth_user_only
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


@auth_user_only
def delete_lesson(request, pk):
    if request.method == "POST":
        lesson = Lesson.objects.filter(id=int(pk))
        lesson.delete()
    lessons = Lesson.objects.all()
    form = CreateLessonForm(request.POST)
    return redirect('/lessons')


@auth_user_only
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


@auth_user_only
def profile(request):
    if request.user.role == student:
        our_student = Student.objects.filter(id=request.user.id).first()
        form = ProfileUserForm(initial={"first_name": our_student.first_name
            , "last_name": our_student.last_name
            , "patronymic": our_student.patronymic
            , "email": our_student.email})
        return render(request, "profile.html",
                      {"form": form, "user": our_student, "role": "student",
                       "group": StudyGroup.objects.filter(student=our_student).first().group_title})
    elif request.user.role == teacher:
        our_teacher = Teacher.objects.filter(id=request.user.id).first()
        form = ProfileUserForm(initial={"first_name": our_teacher.first_name
            , "last_name": our_teacher.last_name
            , "patronymic": our_teacher.patronymic
            , "email": our_teacher.email})
        complete_lessons = our_teacher.count_of_lessons
        loaded_lessons = our_teacher.count_of_completed_lessons
        if complete_lessons != 0:
            counted = (loaded_lessons / complete_lessons) * 100
        else:
            counted = 0
        return render(request, "profile.html",
                      {"form": form, "user": our_teacher, "user": request.user, "role": "teacher",
                       "completed_lessons": complete_lessons, "loaded_lessons": loaded_lessons, "count" : counted})
    return render(request, "profile.html", {"user": request.user})


@auth_user_only
@admin_only
def list_lessons_for_choose_teacher(request):
    if request.method == "GET":
        lessons = Lesson.objects.all()
        return render(request, "lessons_and_teachers.html", {"lessons": lessons})


@auth_user_only
@admin_only
def add_teacher_to_lesson(request, lesson_id):
    if request.method == "POST":
        lesson = Lesson.objects.get(id=lesson_id)
        available_teachers = [teacher for teacher in Teacher.objects.all() if teacher not in lesson.teachers.all()]
        return render(request, "add_teacher_to_lesson.html", {"available_teachers": available_teachers,
                                                              "lesson_title": lesson.title,
                                                              "lesson_id": lesson_id})


@auth_user_only
@admin_only
def post_teacher_to_lesson(request, teacher_id, lesson_id):
    teacher = Teacher.objects.get(id=teacher_id)
    Lesson.objects.get(id=lesson_id).teachers.add(teacher)
    lesson = Lesson.objects.get(id=lesson_id)
    available_teachers = [teacher for teacher in Teacher.objects.all() if teacher not in lesson.teachers.all()]
    return render(request, "add_teacher_to_lesson.html", {"available_teachers": available_teachers,
                                                              "lesson_title": lesson.title,
                                                              "lesson_id": lesson_id})



@teacher_and_admin_only
@auth_user_only
def get_finished_lessons(request):
    finished_lessons_without_video = Lesson.objects.filter(finished=True, teachers=request.user, video_uploaded=False)
    return render(request, "finished_lessons.html", {"finished_lessons": finished_lessons_without_video})


@teacher_and_admin_only
@auth_user_only
def upload_video(request, lesson_id):
    if request.method == "POST":
        upload_video_file = request.FILES['video']
        fs = FileSystemStorage()
        fs.save(upload_video_file.name, upload_video_file)
        if file_unique(media_folder="media/", file_name=upload_video_file.name, lesson_id=lesson_id):
            return render(request, "success_file.html")
        else:
            return HttpResponse("ТАКОЙ ВИДОС УЖЕ БЫЛ ЗАГРУЖЕН")