# -*- encoding: utf-8 -*-
'''
Created on Mar 12, 2014
@author: wilfo
'''
from sistema.models import Persona
from django.contrib.auth.models import User
from utilidades.utilsWeb import JsonSuccess,JsonError
from utilidades import mensaje 
import django.utils.simplejson as json
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
'''
Crea o actualiza la tabla de persona.
'''

@login_required
def getUser_id(request):
    user_id = request.session['_auth_user_id']
    #user=User.objects.get(pk=user_id)
    #total=user.Persona.count()
    return HttpResponse(user_id)
def actualizarPersona(request):
    if request.method != 'POST':
        return JsonError(mensaje.errorSolicitud())
    user_id = request.session['_auth_user_id']
    user=User.objects.get(username__exact=request.user.username)

def eliminarPersona(request):
    if request.method != 'POST':
        return JsonError(mensaje.errorSolicitud())
    json_data=request.POST['persona']
    data=json.loads(json_data)
    persona=Persona.objects.get(pk=data['id'])
    try:
        persona.delete()
        return JsonSuccess({'message':mensaje.eliminar('Persona')})
    except:
        return JsonError(mensaje.errorEliminar('Persona'))
        

