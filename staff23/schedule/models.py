from django.db import models
from django.contrib.auth import get_user_model
from tours.models import Vehicle
from  users.models import Profile


User = get_user_model()


class Schedule(models.Model):

    SERVICE_OPTION = (
        ('Tour', 'Тур'),
        ('Personal Tour', 'Индивидуальный тур'),
        ('Square', 'Площадка'),
        ('Relief', 'Рельеф'),
        ('Rental', 'Прокат')
    )

    date_tour = models.DateField(null=False, blank=False, verbose_name='Дата поездки')
    time_start = models.TimeField(null=False, blank=False, verbose_name='Время начала поездки')
    time_finish = models.TimeField(null=False, blank=False, verbose_name='Время окончания поездки')
    content = models.TextField(null=True, blank=True, verbose_name='Информация по записи')
    service_name = models.CharField(choices=SERVICE_OPTION,
                                    default='Tour',
                                    null=False,
                                    verbose_name='Услуга',
                                    max_length=30)
    sale = models.PositiveSmallIntegerField(null=True, default=0, verbose_name='Скидка')  # todo не больше 100
    instructor = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    vehicles = models.ManyToManyField(Vehicle, symmetrical=False, verbose_name='Техника')

    class Meta:
        db_table = 'app_schedule'
        ordering = ['date_tour', 'time_start', 'time_finish']
        indexes = [models.Index(fields=['date_tour', 'time_start', 'time_finish'])]
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

    def __str__(self):
        return f'{self.date_tour} {self.time_start} {self.service_name} {self.content}'
