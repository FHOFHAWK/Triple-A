from core.models import User


def check_if_teacher(username: str):
    obj = User.objects.filter(username=username)
    if obj.role == "teacher":
        return obj
    else:
        return None
