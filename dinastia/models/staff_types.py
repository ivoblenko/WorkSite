from django.db import models

__all__ = [
    'StaffTypes'
]


class StaffTypes(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return self.name