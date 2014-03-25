'''
Created on Mar 18, 2014

@author: wilfo
'''
from django.conf.urls import patterns, url
from sistema.view.view_personal import getUser_id
from sistema.view.view_cargar_escritorio import cargar_user_escritorio
urlpatterns = patterns('',
    url(r'get_usuario/$',getUser_id),
    url(r'cargar_escritorio/$',cargar_user_escritorio),
)