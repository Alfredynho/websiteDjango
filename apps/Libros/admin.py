from django.contrib import admin

from .models import Libros

@admin.register(Libros)
class LibrosAdmin(admin.ModelAdmin):
	model = Libros
	list_display = ('titulo', 'genero', 'autor','estado')