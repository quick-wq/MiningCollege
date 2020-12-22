from django.shortcuts import render


def handler403(request, *args, **argv):
    return render(request, 'errors/403.html', status=404)


def handler404(request, *args, **argv):
    return render(request, 'errors/404.html', status=404)


def handler500(request, *args, **argv):
    return render(request, 'errors/500.html', status=404)


def index(request):
    """ Главная страница сайта """

    return render(request, 'index.html')
