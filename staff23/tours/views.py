from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Vehicle, Price
from .forms import VehicleCreateForm


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
        context['title'] = self.object.nickname
        return context


class VehicleCreateView(CreateView):
    model = Vehicle
    template_name = 'tours/vehicle_create.html'
    form_class = VehicleCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление техники'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class VehicleUpdateView(UpdateView):
    model = Vehicle
    template_name = 'tours/vehicle_update.html'
    context_object_name = 'vehicle'
    form_class = VehicleCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование техники: {self.object.nickname}'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'tours/vehicle_delete.html'
    success_url = reverse_lazy('vehicles')
    context_object_name = 'vehicle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление техники {self.object.nickname}'
        return context


def index(request):
    # t = render_to_string('tours/index.html')
    # return HttpResponse(t)
    return render(request, 'tours/index.html')


def cats(request):
    return render(request, 'base.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Заехал не туда, такой страницы нет!</h1>')
