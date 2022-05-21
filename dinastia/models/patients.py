from django.db import models
from django.urls import reverse


class Patients(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    phone = models.BigIntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return self.surname + " " + self.name[0] + "." + self.patronymic[0] + "."

    @property
    def short_fio(self):
        return self.surname + " " + self.name[0] + "." + self.patronymic[0] + "."

    def get_absolute_url(self):
        return reverse('patient_update', args=[self.id])
