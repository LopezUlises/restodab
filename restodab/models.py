from django.db import models

class Bebida(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre

class Lanch(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre

class Postre(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre

class Guarnicion(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre

class Breackfast(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre

