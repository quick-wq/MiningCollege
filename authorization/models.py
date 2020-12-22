from random import choice
from string import ascii_letters, digits

from django.contrib.auth.models import User
from django.db import models


class ConfirmationCode(models.Model):
    """ Модель для описания кодов подтверждения регистраций пользователя """

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT, null=False)
    code = models.CharField('Код', max_length=8, null=False)

    def __str__(self):
        return f'{self.user.email} - {self.code}'

    @staticmethod
    def get_random_code(max_length=8) -> str:
        """ Функция генерирует случайную строку """

        symbols = ascii_letters + digits

        return ''.join(choice(symbols) for _ in range(max_length))

    class Meta:
        db_table = 'confirmation_code'
        verbose_name = 'Код подтверждения'
        verbose_name_plural = 'Коды подтверждения'


class AuthorizationHistory(models.Model):
    """ Модель для описания историй авторизаций пользователя """

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT, null=False)
    ip = models.GenericIPAddressField('IP адресс', null=False)

    at = models.DateTimeField('Время', auto_now_add=True)

    def __str__(self):
        return f'{self.user.get_full_name} зашел на сайт в {self.at} ({self.ip})'

    class Meta:
        db_table = 'authorization_history'
        verbose_name = 'Авторизация'
        verbose_name_plural = 'История авторизаций'
