from django.db import models
from django.urls import reverse

from dinastia.models.services import Services
from dinastia.models.patients import Patients


class ServicesRendered(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    final_conditional_unit_of_labor = models.FloatField(verbose_name='УЕТ', null=False)

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return self.patient + ' оказано ' + self.service.code + " " + self.service.name

    @staticmethod
    def get_absolute_url():
        return reverse('services-rendered')
