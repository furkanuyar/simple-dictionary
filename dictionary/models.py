from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10)
    meaning = models.TextField()
