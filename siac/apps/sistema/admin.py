from django.contrib import admin
from django.forms import ModelForm
from suit.widgets import EnclosedInput
from .models import *
from suit.admin import SortableModelAdmin
from mptt.admin import MPTTModelAdmin
from suit.admin import SortableTabularInline


# Register your models here.

class PaisAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'iso', 'prefijo']
    search_fields = ['nombre', 'iso', ]


class ProvinciaForm(ModelForm):
    class Meta:
        widgets = {
            # Estilos para los campos de texto
            'nombre': EnclosedInput(prepend='icon-globe', attrs={'placeholder': 'Ingrese el nombre'}),
            #'nombre': TextInput(attrs={'type': 'text', 'placeholder': 'Ingrese el Nombre'}),
            #'nombre': EnclosedInput(prepend='icon-home', append='<input type="button" class="btn"  value="Open link">'),
        }


class ProvinciaAdmin(admin.ModelAdmin):
    form = ProvinciaForm
    list_display = ['nombre', 'pais', 'zonal']
    search_fields = ['nombre', ]
    list_filter = ['pais', ]


class CantonAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'provincia', ]
    search_fields = ['nombre', ]
    list_filter = ['provincia', ]


class ParroquiaAdmin (admin.ModelAdmin):
    list_display = ['nombre', 'canton', 'tipo_parroquia', ]
    search_fields = ['nombre', 'canton', ]


class CiudadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'canton', ]
    search_fields = ['nombre', ]
    list_filter = ['canton', ]


class OpcionMenuAdmin(MPTTModelAdmin, SortableModelAdmin):
    mptt_level_indent = 20
    list_display = ('nombre', 'id', 'descripcion', 'publicado',)
    list_editable = ('publicado',)
    sortable = 'orden'


class MenuRolInline(SortableTabularInline):
    model = MenuRol
    fk_name = 'rol_usuario'
    sortable = 'rol_usuario'
    raw_id_fields = ('opcion_menu',)


class RolUsuarioAdmin(admin.ModelAdmin):
    inlines = [
        MenuRolInline
    ]
    list_display = ('nombre', 'descripcion', 'caduca')
    sortable = 'nombre'


admin.site.register(TipoIdentificacion)
admin.site.register(Genero)
admin.site.register(TipoSangre)
admin.site.register(EstadoCivil)
admin.site.register(TipoEtnia)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Zonal)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Canton, CantonAdmin)
admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Parentesco)
admin.site.register(CategoriaInstitucion)
admin.site.register(TipoInstitucion)
admin.site.register(Institucion)
admin.site.register(NivelInstruccion)
admin.site.register(Cargo)
admin.site.register(Persona)
admin.site.register(OpcionMenu, OpcionMenuAdmin)
admin.site.register(RolUsuario, RolUsuarioAdmin)