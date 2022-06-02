from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.helpers import gender


class User(AbstractUser):
    address = models.TextField()
    phone_number = models.CharField(max_length=12)
    gender = models.CharField(choices=gender.GENDER, default=gender.GENDER[0], max_length=30)
    profile_pic = models.FileField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=False)
    occupation = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50)
    local_govt = models.CharField(max_length=50, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username