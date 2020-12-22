from django.urls import path

from . import views


urlpatterns = [
    # Авторизация, восстановление пароля и выход
    path('', views.login_view, name='authorization'),
    path('registration/', views.registration_view, name='registration'),
    path('registration/step_two/', views.registration_step_two_view, name='registration_step_two'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    path('logout/', views.logout, name='logout')
]
