from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request):
    # t = render_to_string('tours/index.html')
    # return HttpResponse(t)
    return render(request, 'tours/index.html')


def cats(request):
    return HttpResponse('<h2>че то другое</h2>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Заехал не туда, такой страницы нет!</h1>')
