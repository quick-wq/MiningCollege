from django.contrib.auth.models import User


def send_new_password(user, password):
    """ Функция отпраляет новый пароль пользователю """

    user.email_user(
        'Восстановление пароля',
        f'Новый пароль для доступа на сайт: {password}',
        'noreply@example.com',
        fail_silently=False,
    )


def reset(user: User):
    """ Функция создаёт и задаёт новый пароль для пользователя """

    password: str = User.objects.make_random_password()

    send_new_password(user, password)

    user.set_password(password)
    user.save()
