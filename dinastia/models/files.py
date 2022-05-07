from django.db import models
from .inspections import Inspections


class Files(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    inspection = models.ForeignKey(Inspections, on_delete=models.CASCADE)

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return self.name
