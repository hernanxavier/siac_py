/**
 * @class CRM.sistema.personal.view.PersonalGrid
 * @extends IAEN.abstract.Grid
 * requires 
 * @autor Wilfredo Martel S.
 * @date Martes 24 de marzo del 2014. 
 *
 * Description
 * En este componente muestra una grilla con datos.
 *
 **/

Ext.define("IAEN.modules.catalogs.users.view.UsersGrid",{
	extend		: "IAEN.abstract.Grid",
	requires	: [
		"IAEN.modules.sistema.personal.model.Personal",
		"IAEN.modules.sistema.personal.store.Personal"
	],
	
	title		: "Listado de Personas",
	border		: false,
	editable	: true,
	
	initComponent	: function() {
		var me = this;
		me.store = me.store || Ext.create("IAEN.modules.sistema.personal.store.Personal");
		if(this.editable){
			me.plugins = [Ext.create("Ext.grid.plugin.RowEditing")];
		}
	
		me.columns = [
			Ext.create('Ext.grid.RowNumberer'),
			{header:"Name",dataIndex:"name",flex:1,field: 'textfield'},
			{header:"Lastname",dataIndex:"lastname",flex:1,field: 'textfield'}
		];
        
		if(me.full){
			me.columns.push(
				{header:"Email",dataIndex:"email",flex:1,field: 'textfield'},
				{header:"Active",dataIndex:"active",width:50,renderer:this.showActive,scope:this,field: 'checkbox'}
			);
		}
		me.callParent();
	},
	
	showActive	: function(value){
		if(value){
			return "Yes";
		}else{
			return "No";
		}
	}
});