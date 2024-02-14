from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import DateForm
from datetime import datetime, timedelta


def my_view(request):
    # Создаем объект формы с текущей датой в качестве начального значения
    form = DateForm(initial={'date': datetime.now().date()})

    # Проверяем, была ли отправлена форма
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            # Обработка данных формы при отправке
            ...

    # Отображаем шаблон с передачей объекта формы в контексте
    return render(request, 'sched.html', {'form': form})


class DateView(TemplateView):
    template_name = 'sched.html'

    def get_context_data(self, **kwargs):
        if 'today' in self.request.session:
            today = datetime.strptime(self.request.session['today'], '%Y-%m-%d').date()
        else:
            today = datetime.now().date()
            self.request.session['today'] = today.strftime('%Y-%m-%d')

        context = super().get_context_data(**kwargs)
        context['today'] = today
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

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
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
            return self.render_to_response(self.get_context_data())

        return super().dispatch(request, *args, **kwargs)
