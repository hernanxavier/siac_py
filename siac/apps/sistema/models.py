# coding=utf-8

from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.contrib.auth.models import User, Group
#from django.conf import settings
#from sistema.thumbs import ImageWithThumbsField

# Create your models here.


class RolUsuario(models.Model):
    """
    Clase que guarda una lista de todos los roles de usuarios del sistema.
    """
    grupo = models.ForeignKey(Group)
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField()
    caduca = models.DateField()

    class Meta:
        verbose_name_plural = "Roles de Usuarios"

    def __unicode__(self):
        return "%s" % self.nombre


class OpcionMenu(MPTTModel):
    """
    Listado de opciones (Módulos) para los menus
    """
    #menu = models.ForeignKey(Menu, blank=True, null=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='Hijo', verbose_name='Padre')
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(unique=True)
    icono = models.ImageField(upload_to='upload/iconos_menus/', blank=True, )
    shortcut = models.TextField()
    orden = models.IntegerField(default=0)
    controlador = models.CharField(max_length=255)
    ancho_forma = models.IntegerField(default=600)
    alto_forma = models.IntegerField(default=400)
    publicado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Listas de Menus"

    class MPTTMeta:
        order_insertion_by = ['nombre']
        ordering = ('tree_id', 'lft')
        #ordering = ['orden', 'nombre']

    def __unicode__(self):
        return u'%s' % self.nombre


class MenuRol(models.Model):
    """
    Modelo que representa el conjunto de opciones y permisos de las mismas,
    pertenecientes a un Rol de usuario.
    """
    rol_usuario = models.ForeignKey(RolUsuario)
    opcion_menu = models.ForeignKey(OpcionMenu, null=True, blank=True, unique=True)
    crear = models.BooleanField(default=False)
    leer = models.BooleanField(default=False)
    actualizar = models.BooleanField(default=False)
    borrar = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Menus para el Rol actual"

    def __unicode__(self):
        return u"%s %s" % (self.rol_usuario, self.opcion_menu.nombre)


class TipoIdentificacion(models.Model):
    """
    Representa tipos de identificación (CI - Pasaporte)
    """
    nombre_identificacion = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % self.nombre_identificacion

    class Meta:
        verbose_name_plural = "Tipo de Identificación"


class Genero(models.Model):
    """
    Representa el género de una persona: Masculino, Femenino, etc
    """
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % self.nombre

    class Meta:
        verbose_name_plural = "Género"


class TipoSangre(models.Model):
    """
    Representa los diversos tipos de sangre existentes
    """
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % self.nombre

    class Meta:
        verbose_name_plural = "Tipo de Sangre"


class EstadoCivil(models.Model):
    """
    Representa los diferentes estados civiles existentes
    """
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.nombre)

    class Meta:
        verbose_name_plural = "Estado Civil"


class TipoEtnia(models.Model):
    """
    Representa las deniminaciones de etnias
    """
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % self.nombre

    class Meta:
        verbose_name_plural = "Tipo de Etnia"


class Pais(models.Model):
    """
    Guarda los paises
    """
    iso = models.CharField(max_length=10, blank=True, null=True, verbose_name='Código ISO')
    nombre = models.CharField(max_length=100)
    prefijo = models.CharField(max_length=40, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.nombre

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"


class Zonal(models.Model):
    """
    Representa la zonificación que tiene el país de acuerdo
    al ordenamietno territorial de la República del Ecuador
    """
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % self.nombre

    class Meta:
        verbose_name_plural = "Zonales"


class Provincia(models.Model):
    """
    Provincias principalmente de Ecuador y se relaciona con la zonal
    """
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, blank=True, null=True)
    zonal = models.ForeignKey(Zonal, blank=True, null=True)

    def __unicode__(self):
        return "%s , %s" % (self.nombre, self.pais)


class Canton(models.Model):
    """
    Representa los cantones de las provincias del ecuador
    """
    nombre = models.CharField(max_length=100, verbose_name="Cantón")
    provincia = models.ForeignKey(Provincia)

    def __unicode__(self):
        return "%s, %s" % (self.nombre, self.provincia)

    class Meta:
        verbose_name_plural = "Cantones"


class Ciudad(models.Model):
    """
    Representa las ciudades del mundo
    """
    canton = models.ForeignKey(Canton)
    nombre = models.CharField(max_length=200, verbose_name="Ciudad")

    def __unicode__(self):
        return "%s" % self.nombre

    class Meta:
        verbose_name_plural = "Ciudad"


class TipoParroquia(models.Model):
    """
    Clasificación de las parroquias (Rural = 1 * Urbana = 2)
    """
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % self.nombre


class Parroquia(models.Model):
    """
    Parroquias pertenecientes a cada provincia del Ecuador
    """
    nombre = models.CharField(max_length=300, blank=True, null=True)
    tipo_parroquia = models.ForeignKey(TipoParroquia)
    canton = models.ForeignKey(Canton)
    # ciudad = models.ForeignKey(Ciudad)

    def __unicode__(self):
        return "%s, %s, %s" % (self.nombre, self.canton, self.tipo_parroquia)


class Parentesco(models.Model):
    """
    Representa los diferentes tipos de parentesco que un familiar
    o persona tiene con alguien registrado en el sistema
    """
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % self.nombre


class CategoriaInstitucion(models.Model):
    """
    Catergorías de institusiones y empresas
    Ejemplo: Banco, Universidad
    """
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categoría de Institución"


class TipoInstitucion(models.Model):
    """
    Tipos de empresas: Publicas, Privadas...
    """
    nombre = models.CharField(max_length=299)

    def __unicode__(self):
        return "%s" % self.nombre

    class Meta:
        verbose_name_plural = "Tipo de Institución"


class Institucion(models.Model):
    """
    Representa los datos de las instituciones o empresas registradas en el sistema
    @nombre guarda el nombre de una persona
    """
    nombre = models.CharField(max_length=200)
    representante = models.CharField(max_length=200, verbose_name='Representante Legal:', blank=True, null=True)
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion:', blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    telf1 = models.CharField(max_length=20, verbose_name='Telefono 1:', blank=True, null=True)
    telf2 = models.CharField(max_length=20, verbose_name='Telefono 2:', blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad)
    categoria_empresa = models.ForeignKey(CategoriaInstitucion, verbose_name='Categoría')
    tipo_institucion = models.ForeignKey(TipoInstitucion, verbose_name='Tipo de institucion')

    def __unicode__(self):
        return "%s" % self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Institución"


class NivelInstruccion(models.Model):
    """
    Niveles de instruccion educativa que puede tener una persona
    Ejemplo:Primaria, Secundaria
    """
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % self.nombre

    class Meta:
        verbose_name_plural = "Nivel de Instrucción"


class TituloProfesional(models.Model):
    """
    Representa el listado de los títulos profesionales de una persona
    """
    nombre = models.CharField(max_length=300)

    def __unicode__(self):
        return "%s" % self.nombre

    class Meta:
        verbose_name_plural = "Titulos Profesionales"


class Cargo(models.Model):
    """
    Cargos profesionales de personas
    """
    nombre = models.CharField(max_length=300)

    def __unicode__(self):
        return "%s" % self.nombre

    class Meta:
        verbose_name_plural = "Cargos Profesionales"


class Confirmar_Registro(models.Model):
    name = models.CharField(max_length=2)


class Persona(models.Model):
    """
    Representa los datos personales de una persona
    """
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.TextField(null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    telefono_domicilio = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento', blank=True, null=True)
    fecha_registro = models.DateField(verbose_name='Fecha de registro', auto_now=True, blank=True, null=True)

    #número de la casa.
    numero_domicilio = models.CharField(verbose_name='Numero de domicilio', max_length=50, blank=True, null=True)

    #ruc , cedula lo que sea
    numero_identificacion = models.CharField(verbose_name='Número de identificación:', max_length=50)

    #Boolean
    discapacidad = models.BooleanField()

    carnet_conadis = models.CharField(verbose_name='Nro. Carné de CONADIS:', max_length=50, blank=True, null=True)
    porcentaje_discapacidad = models.CharField(verbose_name='Porcentaje de discapacidad:', max_length=3, default='0',
                                               blank=True, null=True)

    #nobre de la persona que se contactará
    contacto_emergencia = models.CharField(verbose_name='Contacto de emergencia:', max_length=200, blank=True,
                                           null=True)

    telefono_emergencia = models.CharField(verbose_name='Teléfono de emergencia:', max_length=20, blank=True, null=True)
    celular_emergencia = models.CharField(verbose_name='Celular de emergencia:', max_length=20, blank=True, null=True)
    email_emergencia = models.CharField(verbose_name='Email para emergencia:', max_length=200, blank=True, null=True)

    #código de acceso de la tarjeta de ingreso
    codigo_acceso = models.CharField(verbose_name='Acceso al IAEN:', max_length=200, blank=True, null=True)

    foto = models.CharField(max_length=300, blank=True, null=True)

    #"estado de la persona: A:Activo , I:Inactivo ,etc "
    estado = models.CharField(verbose_name='Activo:', max_length=2, blank=True, null=True)

    usuario = models.ForeignKey(User, unique=True)

    #especifíca si es cédula , pasaporte...
    tipo_identidad = models.ForeignKey(TipoIdentificacion, blank=True, null=True)

    #con la ciudad se tiene la provincia , país.
    ciudad_nacimiento = models.ForeignKey(Ciudad, related_name='ciudad_nacimiento')

    #ciudad de donde reside la persona actualmente
    ciudad_residencia = models.ForeignKey(Ciudad, related_name='ciudad_residencia')

    #nacionalidad de la personas
    pais_nacimiento = models.ForeignKey(Pais, related_name='pais_nacimiento')
    estado_civil = models.ForeignKey(EstadoCivil)
    tipo_sangre = models.ForeignKey(TipoSangre)

    #genero de las personas
    genero = models.ForeignKey(Genero)

    # etnia de la persona
    etnia = models.ForeignKey(TipoEtnia)

    def __unicode__(self):
        return "%s" % self.nombre

    class Meta:
        verbose_name_plural = "Persona"
