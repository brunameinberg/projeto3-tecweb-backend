from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pontuacao = models.SmallIntegerField(default=0)