from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre= models.CharField(max_length=100)
    edad= models.IntegerField()
    fecha_nacimiento= models.DateField()

    def __str__(self):
        return f'{self.nombre}'