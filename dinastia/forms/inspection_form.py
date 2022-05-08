from django import forms
from ..models.inspections import Inspections


class InspectionForm(forms.ModelForm):
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput({'placeholder': 'family'}))
    name = forms.CharField(label='Имя', max_length=200, widget=forms.TextInput({'placeholder': 'family'}))
    patronymic = forms.CharField(label='Отчество', max_length=200, widget=forms.TextInput({'placeholder': 'family'}))
    phone = forms.IntegerField(label='Телефон', max_value=9999999999, min_value=1000000000,
                               widget=forms.NumberInput({'placeholder': 'phone'}))
    dob = forms.DateField(label='Дата рождения', widget=forms.DateInput({'class': 'datepicker', 'placeholder': 'dob'}))

    class Meta:
        model = Inspections
        fields = ['surname', 'name', 'patronymic', 'phone', 'dob', 'complaints', 'anamnesis', 'diagnosis',
                  'additionally']
