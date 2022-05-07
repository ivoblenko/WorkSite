from django.db import models
from .patients import Patients
from .staffs import Staffs


class Inspections(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    complaints = models.TextField()
    anamnesis = models.TextField()
    diagnosis = models.TextField()
    additionally = models.TextField()

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return 'Осмтор пациента' +self.patient.get_short_fio() + " от " + self.date

    @classmethod
    def get_fields(cls):
        return ['date', 'patient', 'staff', 'complaints', 'anamnesis', 'diagnosis', 'additionally']