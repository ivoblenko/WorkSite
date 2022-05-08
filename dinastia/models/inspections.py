from django.db import models
from .patients import Patients
from .staffs import Staffs
from tinymce import models as tinymce_models


class Inspections(models.Model):
    date = models.DateField('Дата', auto_now=True)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Пациент')
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE, verbose_name='Сотрудник', null=True)
    complaints = tinymce_models.HTMLField('Жалобы', null=True, blank=True)
    anamnesis = tinymce_models.HTMLField('Анамнез', null=True, blank=True)
    diagnosis = tinymce_models.HTMLField('Диагноз', null=True, blank=True)
    additionally = tinymce_models.HTMLField('Дополнительно', null=True, blank=True)

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return 'Осмтор пациента' + self.patient.short_fio + " от " + self.date


    @classmethod
    def get_for_table(cls):
        return cls.objects.values('patient', 'staff', 'date', 'id')
