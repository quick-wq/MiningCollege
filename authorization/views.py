from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from services.user_service import username_check, email_check, registration_user
from services.password_reset import reset

from .forms import RegisterForm, LoginForm, PasswordResetForm


def registration_view(request):
    """ Регистрация в личном кабинете """

    if request.user.is_authenticated:
        return redirect('personal_area')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.data.get('username')
            email = form.data.get('email')
            password = form.data.get('password')
            password_retry = form.data.get('password_retry')

            if not username:
                form.add_error('username', 'Вы не ввели username!')

            if not email:
                form.add_error('email', 'Вы не ввели email!')

            if not password:
                form.add_error('password', 'Вы не ввели password!')

            if not username_check(username):
                form.add_error('username', 'Такое имя пользователя занято!')

            if not email_check(email):
                form.add_error('email', 'Такая почта занята!')

            if not password == password_retry:
                form.add_error('password_retry', 'Вы неверно повторили пароль!')

            if len(form.errors) == 0:
                user = registration_user(username, email, password)
                login(request, user)
                return redirect('registration_step_two')

            else:
                return render(request, 'authorization/registration.html', {'form': form})

    else:
        form = RegisterForm

    return render(request, 'authorization/registration.html', {'form': form})


def registration_step_two_view(request):
    return HttpResponse('registration_step_two')


def login_view(request):
    """ Авторизация в личном кабинете """

    if request.user.is_authenticated:
        return redirect('personal_area')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.data.get('login'), password=form.data.get('password'))

            if user is not None:
                login(request, user)
                if user.is_active:
                    return redirect('personal_area')
                else:
                    return HttpResponse('Ваша учетная запись отключена!')
            else:
                form.add_error('password', 'Имя пользователя или пароль не верен!')
                return render(request, 'authorization/index.html', {'form': form})

    else:
        form = LoginForm

    return render(request, 'authorization/index.html', {'form': form})


def password_reset_view(request):
    """ Восстановление пароля """

    if request.user.is_authenticated:
        return redirect('personal_area')

    if request.method == 'POST':
        form = PasswordResetForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.data.get('authorization'), password_reset=True)

            if user is not None:
                reset(user)
                return render(request, 'authorization/password_reset_done.html')
            else:
                form.add_error('login', 'Пользователь с таким email или username не найден!')
                return render(request, 'authorization/password_reset.html', {'form': form})

    else:
        form = PasswordResetForm

    return render(request, 'authorization/password_reset.html', {'form': form})


def logout_view(request):
    """ Выход из личного кабинета """

    if request.user.is_authenticated:
        logout(request)

    return redirect('index')
