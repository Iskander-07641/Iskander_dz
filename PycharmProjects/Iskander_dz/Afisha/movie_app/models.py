from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import random


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.text} - {self.stars}/5"


class User(AbstractUser):
    # Adding a confirmation code field
    confirmation_code = models.CharField(max_length=6, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='movieapp_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='movieapp_users',
        blank=True
    )

    def generate_confirmation_code(self):
        code = str(random.randint(100000, 999999))
        self.confirmation_code = code
        self.save()

    pass
