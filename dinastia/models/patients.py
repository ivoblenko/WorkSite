from django.db import models


class Patients(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    phone = models.IntegerField()
    dob = models.DateField()

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return self.surname + " " + self.name + " " + self.patronymic

    def get_short_fio(self):
        return self.surname + " " + self.name[0] + " " + self.patronymic[0]