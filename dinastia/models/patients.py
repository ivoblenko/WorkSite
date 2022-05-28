from django.db import models
from django.urls import reverse


class Patients(models.Model):
    surname = models.CharField(max_length=200, verbose_name="Фамилия")
    name = models.CharField(max_length=200, verbose_name="Имя")
    patronymic = models.CharField(max_length=200, verbose_name="Отчество")
    phone = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Номер телефона")
    dob = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    sex = models.PositiveSmallIntegerField(null=True)
    snils = models.PositiveIntegerField(null=True)
    permanent_address = models.TextField(null=True)
    registration_address = models.TextField(null=True)
    contact_person = models.CharField(max_length=200, null=True)
    contact_person_phone = models.PositiveBigIntegerField(null=True, blank=True)

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return self.surname + " " + self.name[0] + "." + self.patronymic[0] + "."

    @property
    def short_fio(self):
        return self.surname + " " + self.name[0] + "." + self.patronymic[0] + "."

    def get_absolute_url(self):
        return reverse('patient_update', args=[self.id])
