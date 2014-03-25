

Ext.Loader.setConfig({
	enabled : true,
	paths   : {
		IAEN : IAEN.BASE_PATH+'IAEN'
	} 
});

Ext.require("IAEN.modules.login.LoginForm");

Ext.onReady(function(){
	var win = Ext.create("IAEN.modules.login.LoginWindow");
	win.show();

	Ext.get("loading").remove();
});