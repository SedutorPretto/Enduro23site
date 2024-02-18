from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .forms import DateForm
from .models import Schedule
from datetime import datetime, timedelta


class ScheduleListView(ListView):
    model = Schedule
    template_name = 'schedule.html'
    context_object_name = 'schedules'

    def get_queryset(self):
        if 'today' in self.request.session:
            today = datetime.strptime(self.request.session['today'], '%Y-%m-%d').date()
        else:
            today = datetime.now().date()
            self.request.session['today'] = today.strftime('%Y-%m-%d')

        return Schedule.objects.filter(date_tour=today)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Расписание'
        context['today'] = datetime.strptime(self.request.session['today'], '%Y-%m-%d').date()
        weekday_names_ru = {
            0: 'понедельник',
            1: 'вторник',
            2: 'среда',
            3: 'четверг',
            4: 'пятница',
            5: 'суббота',
            6: 'воскресенье'
        }

        # Получение дня недели на русском языке
        context['weekday_ru'] = weekday_names_ru[context['today'].weekday()]
        return context

    def post(self, request, *args, **kwargs):
        today = datetime.strptime(self.request.session['today'], '%Y-%m-%d').date()

        if 'prev_date' in request.POST:
            today -= timedelta(days=1)
        elif 'next_date' in request.POST:
            today += timedelta(days=1)
        elif 'new_date' in request.POST:
            new_date = request.POST.get('new_date')
            if new_date:
                today = datetime.strptime(new_date, '%Y-%m-%d').date()

        self.request.session['today'] = today.strftime('%Y-%m-%d')
        return self.get(request, *args, **kwargs)