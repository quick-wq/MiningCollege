from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from django.core.validators import validate_email


class CustomBackend(ModelBackend):
    """ Кастомные бекенд авторизаций реализующий авторизацию по username и email """

    @staticmethod
    def is_email(text: str) -> bool:
        """ Функция проверяет что строка является почтой """

        try:
            validate_email(text)
            return True
        except Exception:
            return False

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        try:
            # если в username находится почта...
            if self.is_email(username):
                user = UserModel.objects.get(email=username)
            else:
                user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None
        else:
            # Если передан password_reset при авторизаций и он True,
            # значит проиходит восстановление пароля, возвращаем юзера не проверяя пароль
            if kwargs.get('password_reset', False):
                return user

            # TODO: Добавить запись в историю авторизаций

            if user.check_password(password):
                return user
        return None
