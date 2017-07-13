from django.db import models

class Consumicion(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='static/img',
                               blank=True,
                               null=True)
    categoria = models.CharField(
        max_length=2,
        choices=(
            ('P', 'Postre'),
            ('L', 'Lunch'),
            ('G', 'Guarnicion'),
            ('D', 'Breakfast'),
            ('B', 'Bebida')
        )
     )

    def __str__(self):
        return self.nombre
