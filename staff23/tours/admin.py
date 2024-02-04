from django.contrib import admin
from .models import Vehicle, Price, VehicleCategory
from mptt.admin import DraggableMPTTAdmin


# Register your models here.


@admin.register(VehicleCategory)
class VehicleCategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'id', 'title', 'slug')
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Основная информация', {'fields': ('title', 'slug', 'parent')}),
    )


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_model', 'nickname', 'status')
    prepopulated_fields = {'slug': ('nickname',)}
    list_display_links = ('nickname',)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('vehicle_model',)}
