from django.db import models

class Comida(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    categoria = models.ForeignKey('Categoria')

class Bebida(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    categoria = models.ForeignKey('Categoria')

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
