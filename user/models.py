from django.contrib.auth.models import User
from django.db import models

import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    uuid = models.CharField(max_length=50, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
