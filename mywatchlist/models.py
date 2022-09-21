from django.db import models

# Create your models here.

class Movie(models.Model):
    is_watched = models.BooleanField()
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.TextField()
    