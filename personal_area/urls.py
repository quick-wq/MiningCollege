from django.urls import path

from . import views


urlpatterns = [
    # Личный кабинет
    path('', views.my, name='personal_area'),
    path('activities', views.my_activities, name='my_activities'),
    path('all_activities', views.all_activities, name='all_activities'),

    # Личный кабинет, дополнение для администраторов
    path('statistics', views.statistics, name='statistics'),
    path('confirmations', views.confirmations, name='confirmations')
]
