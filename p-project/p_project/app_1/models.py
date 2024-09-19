from django.db import models

# Create your models here.
class Reciter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    kitab = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Reciter, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    