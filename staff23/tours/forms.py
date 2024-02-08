from django import forms

from .models import Vehicle, Price, VehicleCategory


class VehicleCreateForm(forms.ModelForm):
    vehicle_model = forms.ModelChoiceField(queryset=Price.objects.all(),
                                           empty_label='Модель не выбрана',
                                           label='Модель')
    category = forms.ModelChoiceField(queryset=VehicleCategory.objects.all(),
                                      empty_label='Категория не выбрана',
                                      label='Категория техники')

    class Meta:
        model = Vehicle
        fields = ('vehicle_model', 'nickname', 'slug', 'status', 'category', 'photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
