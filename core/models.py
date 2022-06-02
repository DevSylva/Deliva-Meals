from django.db import models
from core.helpers import category as cat


class Food(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(choices=cat.CATEGORY, default=cat.CATEGORY[0], max_length=30)
    cook_time = models.CharField(max_length=40)
    price = models.FloatField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    value = models.FloatField(default=0)

    def __str__(self):
        return self.food

    