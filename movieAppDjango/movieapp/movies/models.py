from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    year = models.IntegerField()
    poster = models.TextField()
    homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.title
