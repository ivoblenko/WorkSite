from django.db import models
from django.urls import reverse


class CashReceipts(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование', null=False)

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('cash_receipts')
