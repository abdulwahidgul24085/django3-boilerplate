from django.contrib.auth.models import AbstractUser
from core.models import TimeStampedModel
from django.db import models


class User(AbstractUser, TimeStampedModel):

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created']
