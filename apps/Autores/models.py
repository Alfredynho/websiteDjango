from __future__ import unicode_literals

from django.db import models

class Autor(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	pais = models.CharField(max_length=50)


	def __str__(self):
		return self.nombre