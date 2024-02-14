from django import forms
from datetime import datetime


class DateForm(forms.Form):
    date_on_screen = forms.DateField(initial=datetime.now().date(), widget=forms.DateInput(attrs={'type': 'date'}))
