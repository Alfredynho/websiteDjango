from django.conf.urls import include, url
from .views import ListarView, CrearView, ActualizarView, EliminarView


urlpatterns = [
	url(r'^listar_autores/$',ListarView.as_view(),name='lista_atores'),
	url(r'^create_autores/$',CrearView.as_view(),name='crear_autor'),
	url(r'^editar_autor/(?P<pk>\d+)/$',ActualizarView.as_view(),name='editar_autor'),
	url(r'^eliminar_autor/(?P<pk>\d+)/$',EliminarView.as_view(),name='eliminar_autor'),
]