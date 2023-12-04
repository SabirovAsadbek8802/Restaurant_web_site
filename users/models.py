from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return self.get_full_name()
