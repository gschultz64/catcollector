from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CatToy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    cattoys = models.ManyToManyField(CatToy)

    def __str__(self):
        return self.name
