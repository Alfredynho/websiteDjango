from django.shortcuts import render
from .models import Autor
from django.views.generic import CreateView, UpdateView , DeleteView, ListView
from .forms import AutorForm

class ListarView(ListView):
	model = Autor
	context_object_name = 'autores'
	template_name = 'autores/listar.html'


class CrearView(CreateView):
	model = Autor
	template_name = 'autores/crear.html'
	form_class = AutorForm
	success_url = '/listar_autores'


class ActualizarView(UpdateView):
	form_class = AutorForm
	template_name = 'autores/update.html'
	model = Autor
	success_url='/listar_autores'


class EliminarView(DeleteView):
	model = Autor
	template_name = 'autores/eliminar.html'
	success_url='/listar_autores'
