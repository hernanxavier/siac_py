# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoIdentificacion'
        db.create_table(u'sistema_tipoidentificacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_identificacion', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'sistema', ['TipoIdentificacion'])

        # Adding model 'Genero'
        db.create_table(u'sistema_genero', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'sistema', ['Genero'])

        # Adding model 'TipoSangre'
        db.create_table(u'sistema_tiposangre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'sistema', ['TipoSangre'])

        # Adding model 'EstadoCivil'
        db.create_table(u'sistema_estadocivil', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'sistema', ['EstadoCivil'])

        # Adding model 'TipoEtnia'
        db.create_table(u'sistema_tipoetnia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'sistema', ['TipoEtnia'])

        # Adding model 'Pais'
        db.create_table(u'sistema_pais', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('prefijo', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
        ))
        db.send_create_signal(u'sistema', ['Pais'])

        # Adding model 'Zonal'
        db.create_table(u'sistema_zonal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'sistema', ['Zonal'])

        # Adding model 'Provincia'
        db.create_table(u'sistema_provincia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Pais'], null=True, blank=True)),
            ('zonal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Zonal'], null=True, blank=True)),
        ))
        db.send_create_signal(u'sistema', ['Provincia'])

        # Adding model 'Canton'
        db.create_table(u'sistema_canton', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('provincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Provincia'])),
        ))
        db.send_create_signal(u'sistema', ['Canton'])

        # Adding model 'Ciudad'
        db.create_table(u'sistema_ciudad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('canton', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Canton'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'sistema', ['Ciudad'])

        # Adding model 'Parroquia'
        db.create_table(u'sistema_parroquia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Ciudad'])),
        ))
        db.send_create_signal(u'sistema', ['Parroquia'])

        # Adding model 'Parentesco'
        db.create_table(u'sistema_parentesco', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'sistema', ['Parentesco'])

        # Adding model 'CategoriaInstitucion'
        db.create_table(u'sistema_categoriainstitucion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'sistema', ['CategoriaInstitucion'])

        # Adding model 'TipoInstitucion'
        db.create_table(u'sistema_tipoinstitucion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=299)),
        ))
        db.send_create_signal(u'sistema', ['TipoInstitucion'])

        # Adding model 'Institucion'
        db.create_table(u'sistema_institucion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('representante', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('telf1', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('telf2', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Ciudad'])),
            ('categoria_empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.CategoriaInstitucion'])),
            ('tipo_institucion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.TipoInstitucion'])),
        ))
        db.send_create_signal(u'sistema', ['Institucion'])

        # Adding model 'NivelInstruccion'
        db.create_table(u'sistema_nivelinstruccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'sistema', ['NivelInstruccion'])

        # Adding model 'TituloProfesional'
        db.create_table(u'sistema_tituloprofesional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'sistema', ['TituloProfesional'])

        # Adding model 'Cargo'
        db.create_table(u'sistema_cargo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'sistema', ['Cargo'])

        # Adding model 'Persona'
        db.create_table(u'sistema_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('direccion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('telefono_domicilio', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_registro', self.gf('django.db.models.fields.DateField')(auto_now=True, null=True, blank=True)),
            ('numero_domicilio', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('numero_identificacion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('discapacidad', self.gf('django.db.models.fields.BooleanField')()),
            ('carne_conadis', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('porcentaje_discapacidad', self.gf('django.db.models.fields.CharField')(default='0', max_length=3, null=True, blank=True)),
            ('contacto_emergencia', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('telefono_emergencia', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('celular_emergencia', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('email_emergencia', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('codigo_acceso', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('foto', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('tipo_identidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.TipoIdentificacion'], null=True, blank=True)),
            ('ciudad_nacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ciudad_nacimiento', to=orm['sistema.Ciudad'])),
            ('ciudad_residencia', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ciudad_residencia', to=orm['sistema.Ciudad'])),
            ('pais_nacimiento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pais_nacimiento', to=orm['sistema.Pais'])),
            ('estado_civil', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.EstadoCivil'])),
            ('tipo_sangre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.TipoSangre'])),
            ('genero', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Genero'])),
            ('etnia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.TipoEtnia'])),
        ))
        db.send_create_signal(u'sistema', ['Persona'])

        # Adding model 'Subgrupo'
        db.create_table(u'sistema_subgrupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('estado', self.gf('django.db.models.fields.BooleanField')()),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.Group'])),
        ))
        db.send_create_signal(u'sistema', ['Subgrupo'])

        # Adding model 'Menu'
        db.create_table(u'sistema_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('orden', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('padre', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('url', self.gf('django.db.models.fields.TextField')()),
            ('icono', self.gf('django.db.models.fields.TextField')()),
            ('estado', self.gf('django.db.models.fields.BooleanField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'sistema', ['Menu'])

        # Adding model 'SubgrupoMenu'
        db.create_table(u'sistema_subgrupomenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('crear', self.gf('django.db.models.fields.BooleanField')()),
            ('leer', self.gf('django.db.models.fields.BooleanField')()),
            ('actualizar', self.gf('django.db.models.fields.BooleanField')()),
            ('borrar', self.gf('django.db.models.fields.BooleanField')()),
            ('acceso_directo', self.gf('django.db.models.fields.BooleanField')()),
            ('estado', self.gf('django.db.models.fields.BooleanField')()),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Menu'])),
            ('subgrupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Subgrupo'])),
        ))
        db.send_create_signal(u'sistema', ['SubgrupoMenu'])


    def backwards(self, orm):
        # Deleting model 'TipoIdentificacion'
        db.delete_table(u'sistema_tipoidentificacion')

        # Deleting model 'Genero'
        db.delete_table(u'sistema_genero')

        # Deleting model 'TipoSangre'
        db.delete_table(u'sistema_tiposangre')

        # Deleting model 'EstadoCivil'
        db.delete_table(u'sistema_estadocivil')

        # Deleting model 'TipoEtnia'
        db.delete_table(u'sistema_tipoetnia')

        # Deleting model 'Pais'
        db.delete_table(u'sistema_pais')

        # Deleting model 'Zonal'
        db.delete_table(u'sistema_zonal')

        # Deleting model 'Provincia'
        db.delete_table(u'sistema_provincia')

        # Deleting model 'Canton'
        db.delete_table(u'sistema_canton')

        # Deleting model 'Ciudad'
        db.delete_table(u'sistema_ciudad')

        # Deleting model 'Parroquia'
        db.delete_table(u'sistema_parroquia')

        # Deleting model 'Parentesco'
        db.delete_table(u'sistema_parentesco')

        # Deleting model 'CategoriaInstitucion'
        db.delete_table(u'sistema_categoriainstitucion')

        # Deleting model 'TipoInstitucion'
        db.delete_table(u'sistema_tipoinstitucion')

        # Deleting model 'Institucion'
        db.delete_table(u'sistema_institucion')

        # Deleting model 'NivelInstruccion'
        db.delete_table(u'sistema_nivelinstruccion')

        # Deleting model 'TituloProfesional'
        db.delete_table(u'sistema_tituloprofesional')

        # Deleting model 'Cargo'
        db.delete_table(u'sistema_cargo')

        # Deleting model 'Persona'
        db.delete_table(u'sistema_persona')

        # Deleting model 'Subgrupo'
        db.delete_table(u'sistema_subgrupo')

        # Deleting model 'Menu'
        db.delete_table(u'sistema_menu')

        # Deleting model 'SubgrupoMenu'
        db.delete_table(u'sistema_subgrupomenu')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sistema.canton': {
            'Meta': {'object_name': 'Canton'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.Provincia']"})
        },
        u'sistema.cargo': {
            'Meta': {'object_name': 'Cargo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'sistema.categoriainstitucion': {
            'Meta': {'object_name': 'CategoriaInstitucion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sistema.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            'canton': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.Canton']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'sistema.estadocivil': {
            'Meta': {'object_name': 'EstadoCivil'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sistema.genero': {
            'Meta': {'object_name': 'Genero'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sistema.institucion': {
            'Meta': {'object_name': 'Institucion'},
            'categoria_empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.CategoriaInstitucion']"}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.Ciudad']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'representante': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telf1': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'telf2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tipo_institucion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.TipoInstitucion']"})
        },
        u'sistema.menu': {
            'Meta': {'object_name': 'Menu'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.BooleanField', [], {}),
            'icono': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'orden': ('django.db.models.fields.SmallIntegerField', [], {}),
            'padre': ('django.db.models.fields.SmallIntegerField', [], {}),
            'url': ('django.db.models.fields.TextField', [], {})
        },
        u'sistema.nivelinstruccion': {
            'Meta': {'object_name': 'NivelInstruccion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'sistema.pais': {
            'Meta': {'object_name': 'Pais'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'prefijo': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        u'sistema.parentesco': {
            'Meta': {'object_name': 'Parentesco'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sistema.parroquia': {
            'Meta': {'object_name': 'Parroquia'},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.Ciudad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'sistema.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'carne_conadis': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'celular_emergencia': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'ciudad_nacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ciudad_nacimiento'", 'to': u"orm['sistema.Ciudad']"}),
            'ciudad_residencia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ciudad_residencia'", 'to': u"orm['sistema.Ciudad']"}),
            'codigo_acceso': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'contacto_emergencia': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'discapacidad': ('django.db.models.fields.BooleanField', [], {}),
            'email_emergencia': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.EstadoCivil']"}),
            'etnia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.TipoEtnia']"}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_registro': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'genero': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.Genero']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'numero_domicilio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'numero_identificacion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais_nacimiento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pais_nacimiento'", 'to': u"orm['sistema.Pais']"}),
            'porcentaje_discapacidad': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'telefono_domicilio': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'telefono_emergencia': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tipo_identidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.TipoIdentificacion']", 'null': 'True', 'blank': 'True'}),
            'tipo_sangre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.TipoSangre']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'sistema.provincia': {
            'Meta': {'object_name': 'Provincia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.Pais']", 'null': 'True', 'blank': 'True'}),
            'zonal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.Zonal']", 'null': 'True', 'blank': 'True'})
        },
        u'sistema.subgrupo': {
            'Meta': {'object_name': 'Subgrupo'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.BooleanField', [], {}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'sistema.subgrupomenu': {
            'Meta': {'object_name': 'SubgrupoMenu'},
            'acceso_directo': ('django.db.models.fields.BooleanField', [], {}),
            'actualizar': ('django.db.models.fields.BooleanField', [], {}),
            'borrar': ('django.db.models.fields.BooleanField', [], {}),
            'crear': ('django.db.models.fields.BooleanField', [], {}),
            'estado': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leer': ('django.db.models.fields.BooleanField', [], {}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.Menu']"}),
            'subgrupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sistema.Subgrupo']"})
        },
        u'sistema.tipoetnia': {
            'Meta': {'object_name': 'TipoEtnia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sistema.tipoidentificacion': {
            'Meta': {'object_name': 'TipoIdentificacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_identificacion': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sistema.tipoinstitucion': {
            'Meta': {'object_name': 'TipoInstitucion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '299'})
        },
        u'sistema.tiposangre': {
            'Meta': {'object_name': 'TipoSangre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sistema.tituloprofesional': {
            'Meta': {'object_name': 'TituloProfesional'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'sistema.zonal': {
            'Meta': {'object_name': 'Zonal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['sistema']