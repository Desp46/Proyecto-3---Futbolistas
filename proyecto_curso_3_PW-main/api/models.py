from django.db import models

# Create your models here.

class Futbolista(models.Model):
        
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    fecha_contrato = models.DateField(auto_created=True)
    salario = models.IntegerField()

    