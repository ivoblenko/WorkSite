from django import forms
from ..models.inspections import Inspections


class InspectionForm(forms.ModelForm):
    surname = forms.CharField(label='Фамилия', max_length=200)
    name = forms.CharField(label='Имя', max_length=200)
    patronymic = forms.CharField(label='Отчество', max_length=200)

    class Meta:
        model = Inspections
        fields = ['surname', 'name', 'patronymic', 'complaints', 'anamnesis', 'diagnosis', 'additionally']
