from django.db import models
from django.urls import reverse

from dinastia.models.service_categories import ServiceCategories


class Services(models.Model):
    code = models.CharField(max_length=200, verbose_name='Код', null=False)
    name = models.CharField(max_length=200, verbose_name='Наименование', null=False)
    price = models.FloatField(verbose_name='Цена', null=False)
    conditional_unit_of_labor = models.FloatField(verbose_name='УЕТ', null=False)
    external = models.BooleanField(verbose_name='Внешняя услуга', default=False)
    category = models.ForeignKey(ServiceCategories, on_delete=models.CASCADE, verbose_name='Категория')
    active = models.BooleanField(verbose_name='Активно', null=False, default=True)

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return self.code + " " + self.name

    @staticmethod
    def get_absolute_url():
        return reverse('services')
