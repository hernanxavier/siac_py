# Register your models here.
from django.contrib import admin
from sistema.models import *

class PaisAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'iso','prefijo']
    search_fields = ['nombre','iso',]

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pais','zonal']
    search_fields = ['nombre',]
    list_filter = ['pais', ]

class CantonAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'provincia',]
    search_fields = ['nombre',]
    list_filter = ['provincia', ]

class CiudadAdmin(admin.ModelAdmin):
    list_display = ['nombre','canton',]
    search_fields = ['nombre',]
    list_filter = ['canton', ]




admin.site.register(TipoIdentificacion)
admin.site.register(Genero)
admin.site.register(TipoSangre)
admin.site.register(EstadoCivil)
admin.site.register(TipoEtnia)
admin.site.register(Pais,PaisAdmin)
admin.site.register(Zonal)
admin.site.register(Provincia,ProvinciaAdmin)
admin.site.register(Canton,CantonAdmin)
admin.site.register(Ciudad,CiudadAdmin)
admin.site.register(Parroquia)
admin.site.register(Parentesco)
admin.site.register(CategoriaInstitucion)
admin.site.register(TipoInstitucion)
admin.site.register(Institucion)
admin.site.register(NivelInstruccion)
admin.site.register(Cargo)
admin.site.register(Persona)
admin.site.register(Subgrupo)
admin.site.register(Menu)
admin.site.register(SubgrupoMenu)