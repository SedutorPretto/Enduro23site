from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('date_tour',
                    'time_start',
                    'time_finish',
                    'content',
                    'service_name',
                    'sale',
                    'instructor',
)