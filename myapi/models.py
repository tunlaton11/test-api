from django.db import models

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=60)
#     password = models.CharField(max_length=60)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     age = models.IntegerField()


class Musician(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    born = models.IntegerField()
    country = models.CharField(max_length=150)


def __str__(self):
        return self.name