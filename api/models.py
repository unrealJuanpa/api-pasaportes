from django.db import models
from model_utils.models import *


# Modelos
class Persona(TimeStampedModel, SoftDeletableModel):
    nombres = models.CharField(max_length=250, blank=False, null=False)
    apellidos = models.CharField(max_length=250, blank=False, null=False)
    fechanac = models.DateField(null=False, blank=False)

class Continente(TimeStampedModel, SoftDeletableModel):
    nombre = models.CharField(max_length=128, blank=False, null=False)
    abreviacion = models.CharField(max_length=128, blank=True, null=True)

class Pais(TimeStampedModel, SoftDeletableModel):
    nombre = models.CharField(max_length=128, blank=False, null=False)
    prefijo = models.IntegerField(blank=False, null=False)
    continente = models.ForeignKey(Continente, on_delete=models.RESTRICT)

class Pasaporte(TimeStampedModel, SoftDeletableModel):
    numeropasaporte = models.CharField(max_length=64, null=False, blank=False)
    fechaemision = models.DateField(null=False, blank=False)
    fechavence = models.DateField(null=False, blank=False)
    observaciones = models.TextField(null=False, blank=False)
    persona = models.ForeignKey(Persona, on_delete=models.RESTRICT)
    pais = models.ForeignKey(Pais, on_delete=models.RESTRICT)