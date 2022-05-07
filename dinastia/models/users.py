from django.db import models
from .staffs import Staffs

__all__ = [
    'Users'
]


class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE)

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return self.username
