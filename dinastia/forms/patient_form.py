from django import forms
from ..models.patients import Patients


class PatientForm(forms.ModelForm):
    files = forms.FileField(label='Загрузка файлов', required=False,
                            widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Patients
        fields = ['surname', 'name', 'patronymic', 'phone', 'dob']
        labels = {
            'surname': 'Фамилия',
            'name': 'Имя',
            'patronymic': 'Отчество',
            'phone': 'Телефон',
            'dob': 'Дата рождения'
        }
        widgets = {
            'surname': forms.TextInput({'placeholder': 'family'}),
            'name': forms.TextInput({'placeholder': 'family'}),
            'patronymic': forms.TextInput({'placeholder': 'family'}),
            'phone': forms.NumberInput({'placeholder': 'phone'}),
            'dob': forms.DateInput({'class': 'datepicker', 'placeholder': 'dob'})
        }
