from django.db import models

# Create your models here.
class Pais (models.Model):
    pais = models.CharField(max_length=200)
    chutes = models.SmallIntegerField(default=0)