from django.db import models
from .patients import Patients
from ..django_core_rewrited.files.storage import StorageWithFileNameGeneratedByNumber
import os


def uploat_to(instance, filename):
    return 'dinastia/static/files/patients/{0}/{1}'.format(instance.patient.id, filename)


class Files(models.Model):
    name = models.CharField(max_length=200, blank=True)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    file = models.FileField(
        upload_to=uploat_to,
        default='-', storage=StorageWithFileNameGeneratedByNumber)

    class Meta:
        app_label = 'dinastia'

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    @property
    def url(self):
        return 'files/patient/{0}/{1}'.format(self.patient.id, self.filename)
