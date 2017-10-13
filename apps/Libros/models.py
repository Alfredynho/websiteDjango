from __future__ import unicode_literals

from django.db import models
from apps.Autores.models import Autor

DISPONIBLE = 'DIS'
AGOTADO = 'AG'

ESTADO = (
	(DISPONIBLE,'disponible'),
	(AGOTADO,'agotado'),
	)

class Libros(models.Model):
	titulo = models.CharField(max_length=50)
	genero = models.CharField(max_length=50)
	autor = models.ForeignKey(Autor)
	estado = models.CharField(
        max_length=50,
        choices=ESTADO,
        default=DISPONIBLE,
	)


	def __str__(self):
		return self.titulo