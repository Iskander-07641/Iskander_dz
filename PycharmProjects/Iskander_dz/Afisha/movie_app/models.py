from django.db import models


class Director(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    DoesNotExist = None
    objects = None
    text = models.TextField()
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:50]
