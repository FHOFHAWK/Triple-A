from functools import wraps

from django.http import HttpResponse

from core.models import User
from utils.constants import teacher, admin


def check_if_teacher(user: User):
    if user.role == teacher:
        return user
    else:
        return None


def auth_user_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponse('Вы не авторизированы')
        else:
            return function(request, *args, **kwargs)

    return wrap


def admin_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.role == admin:
            return function(request, *args, **kwargs)
        else:
            return HttpResponse('Данный функционал не доступен')

    return wrap
