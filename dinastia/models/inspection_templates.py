from django.db import models
from django.urls import reverse

from .departments import Departments
from tinymce import models as tinymce_models


class InspectionsTemplates(models.Model):
    template_name = models.CharField('Название', max_length=200)
    department = models.OneToOneField(Departments, on_delete=models.CASCADE)
    complaints = tinymce_models.HTMLField('Жалобы', null=True, blank=True)
    anamnesis = tinymce_models.HTMLField('Анамнез', null=True, blank=True)
    diagnosis = tinymce_models.HTMLField('Диагноз', null=True, blank=True)
    additionally = tinymce_models.HTMLField('Дополнительно', null=True, blank=True)

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return 'Шаблон ' + self.template_name

    def get_absolute_url(self):
        return reverse('inspection_template_update', args=[str(self.id)])
