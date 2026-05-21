from django.urls import path
from .views import (
    InicioView,
    MascotaListView, MascotaDetailView, MascotaCreateView, MascotaUpdateView, MascotaDeleteView,
    CitaListView, CitaDetailView, CitaCreateView, CitaUpdateView, CitaDeleteView,
)

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),

    path('mascotas/', MascotaListView.as_view(), name='mascota_list'),
    path('mascotas/nueva/', MascotaCreateView.as_view(), name='mascota_create'),
    path('mascotas/<int:pk>/', MascotaDetailView.as_view(), name='mascota_detail'),
    path('mascotas/<int:pk>/editar/', MascotaUpdateView.as_view(), name='mascota_update'),
    path('mascotas/<int:pk>/eliminar/', MascotaDeleteView.as_view(), name='mascota_delete'),

    path('citas/', CitaListView.as_view(), name='cita_list'),
    path('citas/nueva/', CitaCreateView.as_view(), name='cita_create'),
    path('citas/<int:pk>/', CitaDetailView.as_view(), name='cita_detail'),
    path('citas/<int:pk>/editar/', CitaUpdateView.as_view(), name='cita_update'),
    path('citas/<int:pk>/eliminar/', CitaDeleteView.as_view(), name='cita_delete'),
]