# -*- encoding: utf-8 -*-

from .models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import Registro_Usuario
from django.core.mail import send_mail
from base64 import encodestring, decodestring


# Create your views here.


def Inicio(request):
    return render_to_response('sistema/inicio.html', context_instance=RequestContext(request))


def Registro(request):
    if request.method == 'POST':
        form = Registro_Usuario(request.POST)
        if form.is_valid():
            #cd = form.cleaned_data
            name_user = form.cleaned_data['usuario']
            name = form.cleaned_data['nombre']
            last = form.cleaned_data['apellido']
            email_user = form.cleaned_data['email']
            pass_user = form.cleaned_data['passwd1']
            create_user = User.objects.create_user(username=name_user, first_name=name,
                                                   last_name=last, email=email_user, password=pass_user)
            create_user.is_staff = False
            create_user.is_active = False
            try:
                create_user.save()
                send_mail('Registro SIAC', 'Para completar su registro, por favor, ingrese al siguiente link: ' +
                            '%sactivar_usuario/?query=%s' % (request.META['HTTP_REFERER'],
                                                                     encodestring(email_user)),
                            'hernanxavierp@gmail.com', [email_user], fail_silently=False)
                return HttpResponseRedirect('/')
            except:
                return HttpResponseRedirect('/')
    else:
        form = Registro_Usuario()
    return render_to_response('sistema/registro.html', {'form': form}, context_instance=RequestContext(request))


def Activar_Cuenta(request):
    cadena = request.GET['query'] #se obtiene el correo
    email_user = decodestring(cadena) #desencrypta el correo
    user = User.objects.get(email__exact=email_user)
    user.is_active = True
    user.save()
    return HttpResponseRedirect('/')

