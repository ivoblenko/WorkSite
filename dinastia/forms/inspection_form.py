from django import forms
from ..models.inspections import Inspections
from WorkSite.settings import DATE_INPUT_FORMATS


class InspectionForm(forms.ModelForm):
    # surname = forms.CharField(label='Фамилия', widget=forms.TextInput({'placeholder': 'family'}))
    # name = forms.CharField(label='Имя', max_length=200, widget=forms.TextInput({'placeholder': 'family'}))
    # patronymic = forms.CharField(label='Отчество', max_length=200, widget=forms.TextInput({'placeholder': 'family'}))
    # phone = forms.IntegerField(label='Телефон', max_value=9999999999, min_value=1000000000,
    #                            widget=forms.NumberInput({'placeholder': 'phone'}), required=False)
    # dob = forms.DateField(label='Дата рождения', input_formats=DATE_INPUT_FORMATS,
    #                       widget=forms.DateInput({'class': 'datepicker', 'placeholder': 'dob'}),
    #                       required=False)
    files = forms.FileField(label='Загрузка файлов', required=False,
                            widget=forms.ClearableFileInput(attrs={'multiple': True}))
    print = forms.BooleanField(label='Напечатать осмотр', required=False)

    class Meta:
        model = Inspections
        fields = ['patient', 'complaints', 'anamnesis', 'diagnosis',
                  'additionally', 'files', 'print']
        # widgets = {
        #     'patient': forms.Select({'class': '.patient_select2'})
        # }
