/**
 * @class IAEN.modules.catalogs.users.controller.Personal
 * @extends Ext.app.Controller
 * requires 
 * @autor Wilfredo Martel S.
 * @date Lunes 24 de marzo del 2014.
 *
 * Description
 * Controlador
 *
 **/

Ext.define("IAEN.modules.sistema.personal.controller.Personal",{
	extend		: "IAEN.abstract.Controller",
	views		: [
		"IAEN.modules.sistema.personal.view.Viewport",//yala
		"IAEN.modules.sistema.personal.view.PersonalForm",//yala
	],
	models		: ["IAEN.modules.sistema.personal.model.Personal"],
	//stores		: ["IAEN.modules.sistema.personal.store.Personal"],
	init	: function(){
		this.callParent();
		
	},
	setViewport		: function(){
        this.win.add(Ext.create("IAEN.modules.sistema.personal.view.Viewport"));
	}
});