from django import forms
from ..models.patients import Patients


class PatientForm(forms.ModelForm):
    files = forms.FileField(label='Загрузка файлов', required=False,
                            widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Patients
        fields = '__all__'
        required = (
            'surname',
            'name',
            'patronymic',
            'dob'
        )
        labels = {
            'surname': 'Фамилия',
            'name': 'Имя',
            'patronymic': 'Отчество',
            'sex': ' Пол',
            'dob': 'Дата рождения',
            'snils': 'Снилс',
            'permanent_address': 'Адрес постоянного места жительства',
            'registration_address': 'Адрес регистрации по месту пребывания',
            'phone': 'Телефон',
            'contact_person': 'ФИО',
            'contact_person_phone': 'Телефон'
        }
        widgets = {
            'surname': forms.TextInput({'placeholder': 'family'}),
            'name': forms.TextInput({'placeholder': 'family'}),
            'patronymic': forms.TextInput({'placeholder': 'family'}),
            'sex': forms.Select(choices=((0, 'муж.'),
                                         (1, 'жен.'))),
            'dob': forms.DateInput({'class': 'datepicker', 'placeholder': 'dob'}),
            'snils': forms.NumberInput({'placeholder': 'snils'}),
            'permanent_address': forms.TextInput({'placeholder': 'permanent_address'}),
            'registration_address': forms.TextInput({'placeholder': 'registration_address'}),
            'phone': forms.NumberInput({'placeholder': 'phone'}),
            'contact_person': forms.TextInput({'placeholder': 'contact_person'}),
            'contact_person_phone': forms.NumberInput({'placeholder': 'contact_person_phone'}),
        }

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(PatientForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['registration_address'].required = False
        self.fields['contact_person'].required = False
        self.fields['contact_person_phone'].required = False