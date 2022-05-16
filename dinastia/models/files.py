from django.db import models
from .inspections import Inspections
from ..django_core_rewrited.files.storage import StorageWithFileNameGeneratedByNumber
import os


def uploat_to(instance, filename):
    return 'dinastia/static/files/inspections/{0}/{1}'.format(instance.inspection.id, filename)


class Files(models.Model):
    name = models.CharField(max_length=200, blank=True)
    inspection = models.ForeignKey(Inspections, on_delete=models.CASCADE)
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
        return 'files/inspections/{0}/{1}'.format(self.inspection.id, self.filename)
