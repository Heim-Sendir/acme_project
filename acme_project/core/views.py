from django.shortcuts import render


def page_not_found(request, exception):
    template = 'core/404.html'
    return render(request, template, status=404)


def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html', status=403)
