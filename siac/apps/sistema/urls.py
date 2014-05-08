__author__ = 'xavier'

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',


    url(r'^inicio/$', 'apps.sistema.views.Inicio', name='inicio'),
    url(r'^activar_usuario/', 'apps.sistema.views.Activar_Cuenta', name='activar'),
    url(r'^$', 'apps.sistema.views.Registro', name='registro'),



)