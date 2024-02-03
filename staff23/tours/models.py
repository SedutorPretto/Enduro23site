from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel, TreeForeignKey


User = get_user_model()


class Vehicle(models.Model):

    STATUS_OPTION = (
        ('A', 'Готов к работе'),
        ('C', 'Есть проблемы'),
        ('F', 'На ремонте'),
        ('Z', 'Мехзона воскресит за дорого')
    )

    vehicle_model = models.ForeignKey('Price', on_delete=models.PROTECT)
    nickname = models.CharField(verbose_name='Идентификатор', max_length=30)
    slug = models.SlugField(verbose_name='Альт.название', max_length=255, blank=True, unique=True)
    status = models.CharField(choices=STATUS_OPTION, default='ok', verbose_name='Состояние', max_length=15)
    photo = models.ImageField(verbose_name='Фото техники',
                              blank=True,
                              upload_to='images/vehicle/%Y/%m/%d',
                              default='images/vehicle/default.jpg',
                              validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])
    category = TreeForeignKey('VehicleCategory',
                              verbose_name='Категория',
                              on_delete=models.PROTECT,
                              related_name='vehicles')

    class Meta:
        db_table = 'app_vehicles'
        ordering = ['status']
        indexes = [models.Index(fields=['status'])]
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

    def __str__(self):
        return f'{self.vehicle_model} #{self.nickname}, {self.status}'

    def get_absolure_url(self):
        return reverse('vehicles_detail', kwargs={'slug': self.slug})


class Price(models.Model):
    vehicle_model = models.CharField(verbose_name='Модель', max_length=255, unique=True, db_index=True)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    ground = models.PositiveIntegerField(verbose_name='Площадка в час', blank=True, null=True)
    terrain = models.PositiveIntegerField(verbose_name='Рельеф в час', blank=True, null=True)
    tour = models.PositiveIntegerField(verbose_name='Тур в час', blank=True, null=True)

    def __str__(self):
        return self.vehicle_model

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайс'


class VehicleCategory(MPTTModel):
    title = models.CharField(verbose_name='Название категории', max_length=150, unique=True)
    slug = models.SlugField(verbose_name='URL категории', max_length=255, blank=True, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
        verbose_name='Родительская категория'
    )

    class MPTTMeta:
        order_insertion_by = ('title',)

    class Meta:
        verbose_name = 'Категория техники'
        verbose_name_plural = 'Категории техники'
        db_table = 'app_vehicle_categories'

    def __str__(self):
        return self.title
