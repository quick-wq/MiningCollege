from django.shortcuts import render, redirect


def my(request):
    """ Личный кабинет """

    if request.user.is_authenticated:
        return render(request, 'personal_area/index.html', {'user': request.user, 'view': 'personal_area'})

    return redirect('authorization')


def my_activities(request):
    """ Личный кабинет - мой мероприятия """

    if request.user.is_authenticated:
        return render(request, 'personal_area/my_activities.html', {'user': request.user, 'view': 'my_activities'})

    return redirect('authorization')


def all_activities(request):
    """ Личный кабинет - все мероприятия """

    if request.user.is_authenticated:
        return render(request, 'personal_area/all_activities.html', {'user': request.user, 'view': 'all_activities'})

    return redirect('authorization')


def statistics(request):
    """ Личный кабинет - статистика (только для администраторов) """

    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request, 'personal_area/statistics.html', {'user': request.user, 'view': 'statistics'})
        else:
            return render(request, 'errors/403.html')

    return redirect('authorization')


def confirmations(request):
    """ Личный кабинет - подтверждения (только для администраторов) """

    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request, 'personal_area/confirmations.html', {'user': request.user, 'view': 'confirmations'})
        else:
            return render(request, 'errors/403.html')

    return redirect('authorization')
