from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    semestre = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)