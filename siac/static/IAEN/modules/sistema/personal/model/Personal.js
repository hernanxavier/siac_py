/**
 * @class CRM.sistema.personal.model.Persona
 * @extends Ext.data.Model
 * requires 
 * @autor Wilfredo Martel S.
 * @date Lunes 24 de marzo del 2014. 
 *
 * Description
 * Definimos nuestro modelo a utiliar durante toda la clase.
 *
 **/

Ext.define("IAEN.modules.sistema.personal.model.Personal",{
	extend		: "Ext.data.Model",

	idProperty	: "id",
	fields		: [
		{name:"id",type:"int"},
		{name:"nombre",type:"string"},
		{name:"apellido",type:"string"},
		{name:"direccion",type:"string"},
		{name:"telefono",type:"string"},
		{name:"telefono_domicilio",type:"string"},
		{name:"celular",type:"string"},
		{name:"fecha_nacimiento",type:"date"},
		//{name:"fecha_registro",type:"string"}
		{name:"numero_domicilio",type:"string"},
		{name:"numero_identificacion",type:"string"},
		{name:"discapacidad",type:"boolean"},
		{name:"porcentaje_discapacidad",type:"float"},
		{name:"contacto_emergencia",type:"string"},
		{name:"telefono_emergencia",type:"string"},
		{name:"celular_emergencia",type:"string"},
		{name:"email_emergencia",type:"string"},
		//{name:"codigo_acceso",type:"string"}
		{name:"foto",type:"string"},
		//{name:"estado",type:"string"},
		//{name:"usuario_id",type:"string"}, lo cogo de la sesión
		{name:"tipo_identidad_id",type:"int"},
		{name:"ciudad_nacimiento_id",type:"int"},
		{name:"ciudad_residencia_id",type:"int"},
		{name:"estado_civil_id",type:"int"},
		{name:"tipo_sangre_id",type:"int"},
		{name:"genero_id",type:"int"},
		{name:"etnia_id",type:"int"},
		{name:"pais_nacimiento_id",type:"int"}
	]
	
});