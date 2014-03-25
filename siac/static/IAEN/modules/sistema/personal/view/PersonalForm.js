/**
 * @class CRM.sistema.personal.view.PersonalForm
 * @extends IAEN.abstract.Grid
 * requires 
 * @autor Wilfredo Martel S.
 * @date Martes 24 de marzo del 2014. 
 *
 * Description
 * En este componente muestra una grilla con datos.
 *
 **/
Ext.define("IAEN.modules.sistema.personal.view.PersonalForm",{
	extend		: "IAEN.abstract.Form",
	

	initComponent	: function() {
		var me = this;
		
        me.items = this.buildItems();

		me.callParent();
	},
	
	buildItems		: function(){
		return	{
			xtype	: "fieldset",
			padding	: 10,
			defaults	: {xtype:"textfield",anchor	: '60%'},
			items	: [{
				xtype		: "hidden",
				name		: "id"
			},{
				xtype		:"textfield",
				labelAlign	: "left",
				msgTarget	: 'side',
				fieldLabel	: "Nombre",
				name		: "nombre",
				allowBlank	: false,
				flex		: 1,
				margins		: {right:3},
				maxLength  : 10,
        		enforceMaxLength :10
			},{
				xtype		:"textfield",
				labelAlign	: "left",
				msgTarget	: 'side',
				fieldLabel	: "Apellido",
				name		: "apellido",
				allowBlank	: false,
				flex		: 1,
				margins		: {right:3},
				maxLength  : 10,
        		enforceMaxLength :10
			},{
				xtype		: "textarea",
				fieldLabel	: "Dirección",
				name		: "direccion"
			}]
		};
	}
});