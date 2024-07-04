from django.db import models
from django.contrib.auth.models import User

class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return self.album_name
