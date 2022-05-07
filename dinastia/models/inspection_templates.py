from django.db import models
from .departments import Departments


class InspectionsTemplates(models.Model):
    template_name = models.CharField(max_length=200)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, unique=True)
    complaints = models.TextField()
    anamnesis = models.TextField()
    diagnosis = models.TextField()
    additionally = models.TextField()

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return 'Шаблон ' + self.template_name
