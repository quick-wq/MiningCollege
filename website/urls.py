from django.urls import path

from . import views


urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),

    # Страницы ошибок, тут только для дебага
    path('403', views.handler403, name='error403'),
    path('404', views.handler404, name='error404'),
    path('500', views.handler500, name='error500'),
]
