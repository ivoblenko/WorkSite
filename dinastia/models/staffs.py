from django.db import models
from .staff_types import StaffTypes
from .departments import Departments


class Staffs(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    staff_type = models.ForeignKey(StaffTypes, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return self.surname + " " + self.name[0] + "." + self.patronymic[0] + "."

    @property
    def short_fio(self):
        return self.surname + " " + self.name[0] + "." + self.patronymic[0] + "."
