from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()


class Profile(models.Model):

    POSITION_OPTION = (
        ('INS', 'Инструктор'),
        ('MECH', 'Механик'),
        ('MARKET', 'Магазин'),
        ('ADMIN', 'Администрация')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='images/avatar/%Y/%m/%d',
        default='images/avatar/default.jpg',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))]
    )
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    bio = models.TextField(blank=True, verbose_name='Регалии')
    phone = models.PositiveBigIntegerField(null=True, blank=True, unique=True)
    position = models.CharField(choices=POSITION_OPTION, default='INS', verbose_name='Подразделение', max_length=5000)

    class Meta:
        db_table = 'app_profiles'
        ordering = ('user',)
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'slug': self.slug})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
