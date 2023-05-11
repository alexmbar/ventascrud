from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripción = models.TextField(blank=True)
    precio= models.IntegerField()
    fecha_registro = models.DateTimeField(null=True)
    estatus = models.BooleanField(default=False)