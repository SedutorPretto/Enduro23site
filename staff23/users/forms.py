from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email адрес должен быть уникальным, как твой стиль')
        return email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('slug', 'avatar', 'birth_date', 'bio', 'phone', 'position')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs['placeholder'] = 'Логин сотрудника'
            self.fields['password'].widget.attrs['placeholder'] = 'Пароль сотрудника'
            self.fields['username'].label = 'Логин'
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })