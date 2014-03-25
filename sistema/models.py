# coding=utf-8

from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class TipoIdentificacion(models.Model):
    """
    Representa tipos de identificación (CI - Pasaporte)
    """
    nombre_identificacion = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "%s" %(self.nombre_identificacion)
    class Meta:
        verbose_name_plural = "Tipo de Identificación"


class Genero(models.Model):
    """
    Representa el género de una persona: Masculino, Femenino, etc
    """
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "%s" %(self.nombre)
    class Meta:
        verbose_name_plural = "Género"



class TipoSangre(models.Model):
    """
    Representa los diversos tipos de sangre existentes
    """
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "%s" %(self.nombre)

    class Meta:
        verbose_name_plural = "Tipo de Sangre"


class EstadoCivil(models.Model):
    """
    Representa los diferentes estados civiles existentes
    """
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return "%s" %(self.nombre)
    class Meta:
        verbose_name_plural = "Estado Civil"


class TipoEtnia(models.Model):
    """
    Representa las deniminaciones de etnias
    """
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "%s" %(self.nombre)
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
        return "%s" %(self.nombre)

    class Meta:
        verbose_name="País"
        verbose_name_plural = "Países"


class Zonal(models.Model):
    """
    Representa la zonificación que tiene el país de acuerdo
    al ordenamietno territorial de la República del Ecuador
    """
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "%s" %(self.nombre)
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
        return "%s , %s" %(self.nombre , self.pais)


class Canton(models.Model):
    """
    Representa los cantones de las provincias del ecuador
    """
    nombre = models.CharField(max_length=100,verbose_name="Cantón")
    provincia = models.ForeignKey(Provincia)
    
    def __unicode__(self):
        return "%s %s" %(self.nombre,self.provincia)
    class Meta:
        verbose_name_plural = "Cantones"


class Ciudad(models.Model):
    """
    Representa las ciudades del mundo
    """
    canton = models.ForeignKey(Canton)
    nombre = models.CharField(max_length=200,verbose_name="Ciudad")
    
    def __unicode__(self):
        return "%s" %(self.nombre)
    
    class Meta:
        verbose_name_plural = "Ciudad"


class Parroquia(models.Model):
    """
    Parroquias pertenecientes a las ciudades del Ecuador
    """
    nombre = models.CharField(max_length=300)
    ciudad = models.ForeignKey(Ciudad)
    def __unicode__(self):
        return "%s" %(self.nombre)

class Parentesco(models.Model):
    """
    Representa los diferentes tipos de parentesco que un familiar
    o persona tiene con alguien registrado en el sistema
    """
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return "%s" %(self.nombre)


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
        return "%s" %(self.nombre)
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
        return "%s" %(self.nombre)
    class Meta:
        verbose_name_plural = "Tipos de Institución"


class NivelInstruccion(models.Model):
    """
    Niveles de instruccion educativa que puede tener una persona
    Ejemplo:Primaria, Secundaria
    """
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return "%s" %(self.nombre)
    
    class Meta:
        verbose_name_plural = "Nivel de Instrucción"


class TituloProfesional(models.Model):
    """
    Representa el listado de los títulos profesionales de una persona
    """
    nombre = models.CharField(max_length=300)
    
    def __unicode__(self):
        return "%s" %(self.nombre)
    
    class Meta:
        verbose_name_plural = "Titulos Profesionales"


class Cargo(models.Model):
    """
    Cargos profesionales de personas
    """
    nombre = models.CharField(max_length=300)
    
    def __unicode__(self):
        return "%s" %(self.nombre)
    
    class Meta:
        verbose_name_plural = "Cargos Profesionales"

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

    carne_conadis = models.CharField(verbose_name='Nro. Carné de CONADIS:', max_length=50, blank=True, null=True)
    porcentaje_discapacidad = models.CharField(verbose_name='Porcentaje de discapacidad:', max_length=3, default='0', blank=True, null=True)

    #nobre de la persona que se contactará
    contacto_emergencia = models.CharField(verbose_name='Contacto de emergencia:', max_length=200, blank=True, null=True)

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
        return "%s" %(self.nombre)
    
    class Meta:
        verbose_name_plural = "Persona"

class Subgrupo(models.Model):
    """
    Representan los diferentes Grupos Funcionarios de la institución
    Ejemplo: Directores, Docentes, Contador ...
    """
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    #Activa o desactiva un Subgrupo
    estado = models.BooleanField()
    grupo = models.ForeignKey(Group)

    def __unicode__(self):
        return "%s" %(self.nombre)
    

class Menu(models.Model):
    """
    Modelo que contiene el listado gerárquico de menús
    Ejemplo: Archivo->
                Abrir
                Guardar
                Recientes->
                    uno.txt
                    dos.txt
            Salir
    """
    nombre = models.CharField(max_length=100)
    orden = models.SmallIntegerField()
    padre = models.SmallIntegerField()
    url = models.TextField()
    icono = models.TextField()

    #Valor para menu activo o inactivo
    estado = models.BooleanField()

    descripcion = models.TextField()
    def __unicode__(self):
        return "%s" %(self.nombre)
    
    class Meta:
        verbose_name_plural = "Menus"



class SubgrupoMenu(models.Model):
    """
    Establece una relacion muchos a muchos entre los modelos
    Subgrupo y Menu, almacena el listado de opciones de menu para
    cada Subgrupo con los permisos (CRUD) pertinentes
    """
    crear = models.BooleanField()
    leer = models.BooleanField()
    actualizar = models.BooleanField()
    borrar = models.BooleanField()
    acceso_directo = models.BooleanField()

    #Valor para menu de un subgrupo activo o inactivo
    estado = models.BooleanField()

    menu = models.ForeignKey(Menu)
    subgrupo = models.ForeignKey(Subgrupo)

    def __unicode__(self):
        return "%s" %(self.menu)
    
    class Meta:
        verbose_name_plural = "SubgrupoMenu"