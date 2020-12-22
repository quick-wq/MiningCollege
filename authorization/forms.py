from django import forms

from crispy_forms.helper import FormHelper


class RegisterForm(forms.Form):
    """ Форма для регистраций пользователей """

    username = forms.CharField(label='Юзернейм', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Юзернейм'}))
    email = forms.CharField(label='Почта', widget=forms.TextInput(
        attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Электронная почта'}))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password_retry = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False  # Убираем label (название поля)


class LoginForm(forms.Form):
    """ Форма авторизаций пользователя """

    login = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'email или username'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'password'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False  # Убираем label (название поля)


class PasswordResetForm(forms.Form):
    """ Форма востановления пароля """

    login = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'email или username'}))

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False  # Убираем label (название поля)
