from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Mascota, Cita
from .forms import MascotaForm, CitaForm


class InicioView(TemplateView):
    template_name = 'citas/inicio.html'


class MascotaListView(ListView):
    model = Mascota
    template_name = 'citas/mascota_list.html'
    context_object_name = 'mascotas'


class MascotaDetailView(DetailView):
    model = Mascota
    template_name = 'citas/mascota_detail.html'
    context_object_name = 'mascota'


class MascotaCreateView(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'citas/mascota_form.html'
    success_url = reverse_lazy('mascota_list')


class MascotaUpdateView(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'citas/mascota_form.html'
    success_url = reverse_lazy('mascota_list')


class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = 'citas/mascota_confirm_delete.html'
    success_url = reverse_lazy('mascota_list')


class CitaListView(ListView):
    model = Cita
    template_name = 'citas/cita_list.html'
    context_object_name = 'citas'


class CitaDetailView(DetailView):
    model = Cita
    template_name = 'citas/cita_detail.html'
    context_object_name = 'cita'


class CitaCreateView(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'citas/cita_form.html'
    success_url = reverse_lazy('cita_list')


class CitaUpdateView(UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = 'citas/cita_form.html'
    success_url = reverse_lazy('cita_list')


class CitaDeleteView(DeleteView):
    model = Cita
    template_name = 'citas/cita_confirm_delete.html'
    success_url = reverse_lazy('cita_list')