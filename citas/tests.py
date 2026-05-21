from django.test import TestCase
from django.urls import reverse
from .models import Mascota, Cita
from datetime import date, time


class MascotaModelTest(TestCase):
    def test_crear_mascota(self):
        mascota = Mascota.objects.create(
            nombre='Luna',
            especie='Perro',
            raza='Criollo',
            edad=3,
            propietario='Carlos'
        )

        self.assertEqual(mascota.nombre, 'Luna')
        self.assertEqual(mascota.especie, 'Perro')
        self.assertEqual(mascota.propietario, 'Carlos')


class CitaModelTest(TestCase):
    def test_crear_cita(self):
        mascota = Mascota.objects.create(
            nombre='Max',
            especie='Gato',
            raza='Persa',
            edad=2,
            propietario='Ana'
        )

        cita = Cita.objects.create(
            mascota=mascota,
            fecha=date.today(),
            hora=time(10, 30),
            tipo_cita='Vacunación',
            descripcion='Aplicación de vacuna anual',
            estado='Pendiente'
        )

        self.assertEqual(cita.mascota.nombre, 'Max')
        self.assertEqual(cita.tipo_cita, 'Vacunación')
        self.assertEqual(cita.estado, 'Pendiente')


class VistasTest(TestCase):
    def test_inicio_status_code(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

    def test_lista_mascotas_status_code(self):
        response = self.client.get(reverse('mascota_list'))
        self.assertEqual(response.status_code, 200)

    def test_lista_citas_status_code(self):
        response = self.client.get(reverse('cita_list'))
        self.assertEqual(response.status_code, 200)