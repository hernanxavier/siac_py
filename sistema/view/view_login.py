# -*- encoding: utf-8 -*-
'''
Created on Mar 12, 2014

@author: wilfo
'''
# -*- encoding: utf-8 -*-
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from utilidades.utilsWeb import JsonSuccess,JsonError
from django.core.mail import send_mail
from utilidades import mensaje
from base64 import encodestring, decodestring
from django.http.response import HttpResponse
from django.shortcuts import redirect



def login_user(request):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonSuccess({'message':mensaje.loginOK(),'url':'home.html'})
            else:
                return JsonError(mensaje.loginNoActivo())
        else:
            return JsonError(mensaje.loginIncorrecto())
def activar_cuenta(request):
    cadena=request.GET['query'] #se obtiene el correo
    correo=decodestring(cadena) #desencrypta el correo
    user=User.objects.get(email__exact=correo)
    user.is_active=True
    user.save()
    return HttpResponse(mensaje.cuentaActivada())
    
def logout_user(request):
    logout(request)
    return redirect('/')

def registrar_user(request):
    if request.method !='POST':
        JsonError('Petición invalida.')
        
    nombre=request.POST['txt_nombre']
    apellido=request.POST['txt_apellido']
    usuario=request.POST['txt_usuario']
    correo=request.POST['txt_correo']
    clave=request.POST['txt_clave2']
    user=User.objects.create_user(usuario, correo, clave)
    user.first_name=nombre
    user.last_name=apellido
    user.email=correo
    user.is_staff=True
    user.is_active=False
    try:
        user.save()
        send_mail('IAEN informa : Link de activación','%ssistema/activar_usuario/?query=%s'%(request.META['HTTP_REFERER'],encodestring(user.email)), mensaje.correo_institucion(),
        [correo], fail_silently=False)
        return JsonSuccess( { 'message': mensaje.cuentaCreada(),'url':'' } )
    except:
        return JsonError(mensaje.errorCrearCuenta())
    

