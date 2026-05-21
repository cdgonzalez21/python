from django.db import models


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    propietario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Realizada', 'Realizada'),
        ('Cancelada', 'Cancelada'),
    ]

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_cita = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')

    def __str__(self):
        return f"{self.mascota.nombre} - {self.tipo_cita}"