/**
 * @class CRM.sistema.personal.view.Viewport
 * @extends Ext.data.Viewport
 * requires 
 * @autor Wilfredo Martel S.
 * @date Martes 24 de marzo del 2014. 
 *
 * Description
 * En este componente se renderiza las vistas.
 *
 **/

Ext.define("IAEN.modules.sistema.personal.view.Viewport",{
	extend		: "IAEN.abstract.Viewport",
	
	initComponent	: function() {
		var me = this;
		this.items = this.buildItems();
		me.callParent();
	},
	buildItems	: function(){		
		var personalForm = Ext.create("IAEN.modules.sistema.personal.view.PersonalForm",{
			region	: "center"
		});
		
		return [{layout:"border",region:"center",border:true,items:[personalForm]}];
	}
});