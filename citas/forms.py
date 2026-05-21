from django import forms
from .models import Mascota, Cita


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'edad', 'propietario']


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['mascota', 'fecha', 'hora', 'tipo_cita', 'descripcion', 'estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }