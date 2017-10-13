from django.contrib import admin

from .models import Autor

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
	model = Autor
	list_display = ('nombre','apellido', 'pais')