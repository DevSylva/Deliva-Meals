from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.helpers import gender


class User(AbstractUser):
    address = models.TextField()
    phone_number = models.CharField(max_length=12)
    gender = models.CharField(choices=gender.GENDER, default=gender.GENDER[0], max_length=10)
    profile_pic = models.ImageField()
    age = models.PositiveIntegerField()
    occupation = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50)
    local_govt = models.CharField(max_length=50)

    def __str__(self):
        return self.get_full_name()
