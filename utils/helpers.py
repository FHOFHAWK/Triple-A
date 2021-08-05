from core.models import User
from utils.constants import teacher


def check_if_teacher(user: User):
    if user.role == teacher:
        return user
    else:
        return None
