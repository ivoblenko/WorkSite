from django.db import models
from .staffs import Staffs
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'dinastia'

    def __str__(self):
        return self.username
