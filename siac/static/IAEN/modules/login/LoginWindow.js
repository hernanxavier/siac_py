/**
 * @class IAEN.modules.login.LoginPanel
 * @extends IAEN.ui.ModalPanel
 *
 * The login Panel.
 *
 **/


Ext.define("IAEN.modules.login.LoginWindow",{
	extend 			: "IAEN.abstract.ModalWindow",
	requires		: ["IAEN.modules.login.LoginForm"],
	
	layout			: "auto",
	modal			: false,
	width			: 420,
	minHeight		: 300,
	autoHeight      : true,
	closable		: false,
	
	forward			: true,
	
	initComponent: function() {
		
        this.items = this.buildItems();

		this.callParent();
	},
	
	buildItems	: function(){
		return [{
			xtype	: "component",
			html 	: '<img src="'+IAEN.Constants.LOGIN_IMAGE+'" />' 
		},
			Ext.create("IAEN.modules.login.LoginForm",{forward:this.forward})
		];
	}
});