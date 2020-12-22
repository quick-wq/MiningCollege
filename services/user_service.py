from django.contrib.auth import get_user_model
from django.db.models import Avg


def username_check(username: str) -> bool:
    """ Функция проверяет что username свободен """

    UserModel = get_user_model()

    if UserModel.objects.filter(username=username).count() == 0:
        return True

    return False


def email_check(email: str) -> bool:
    """ Функция проверяем что email свободен """

    UserModel = get_user_model()

    if UserModel.objects.filter(email=email).count() == 0:
        return True

    return False


def registration_user(username: str, email: str, password: str):
    """ Функция регистрирует пользователя """

    UserModel = get_user_model()

    user = UserModel.objects.create(username=username, email=email)
    user.set_password(password)
    user.save()

    return user


def average_reputation(more_zero: bool = False) -> float:
    """ Функция возвращает среднюю репутацию пользователей """

    UserModel = get_user_model()

    if more_zero:
        return UserModel.objects.where(UserModel.reputation > 0).aggregate(Avg('reputation'))
    else:
        return UserModel.objects.all().aggregate(Avg('reputation'))
