from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Vehicle, Price


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'tours/vehicle_list.html'
    context_object_name = 'vehicles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Техника проката'
        return context


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'tours/vehicle_detail.html'
    context_object_name = 'vehicle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


def index(request):
    # t = render_to_string('tours/index.html')
    # return HttpResponse(t)
    return render(request, 'tours/index.html')


def cats(request):
    return render(request, 'base.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Заехал не туда, такой страницы нет!</h1>')
