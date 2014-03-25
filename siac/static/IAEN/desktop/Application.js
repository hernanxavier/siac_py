/**
 * @class IAEN.desktop.Application
 * @extends Ext.app.Application
 * requires IAEN.desktop.Desktop
 *
 * The application class
 *
 *
 **/

Ext.define("IAEN.desktop.Application",{
	extend 		: "Ext.app.Application",
	mixins		: {
		observable	: "Ext.util.Observable"
	},
	requires	: [
		"IAEN.desktop.Desktop",
		"IAEN.desktop.Notification",
		"IAEN.desktop.TaskbarContainer",
		"IAEN.desktop.WindowManager"
	],
	
	useQuickTips: true,

	constructor	: function() {
		var me = this;
		
		me.addEvents({
			"ready"	: true
		});

		me.callParent(arguments);
		
		IAEN.Ajax.request({
			url		: IAEN.Constants.DESKTOP_CONFIGURATION_URL,
			scope	: this,
			success	: this.buildDesktop,
			failure	: this.onError
		});

	},
	//aquí entra el array de json para formar el usuario
	buildDesktop	: function(data){
		var me = this;
		console.log("wilfo aqui inicio");
		console.log(data);
		console.log("wilfo aqui final");
        if (me.useQuickTips) {
            Ext.QuickTips.init();
        }
        //pasamos la configuración iniical de los módulos a la variable me.userConfig
		me.userConfig = data;

		me.desktop = new IAEN.desktop.Desktop({userConfig:me.userConfig});
		
		me.viewport = new Ext.container.Viewport({
            layout	: "fit",
            items	: me.desktop
        });

        Ext.EventManager.on(window, "beforeunload", me.onUnload, me);

        me.fireEvent("ready", me);
	},
	
	/**
	 * Execute an application
	 * @param {Ext.menu.Item} item The item licked in the menu
	 */
	runApplication	: function(item) {
		var app = item.initialConfig,
			me	= this;
		
		me.desktop.windowMgr.loader.show();
		IAEN.Ajax.request({
			url		: "sistema/configuracion_user/",
			scope	: me,
			app		: app,
			params	: {
				application_k : app.application_k
			},
			success	: me.showApplication,
			failure	: me.onPermissionsError
		});
		
	},
	
	/**
	 *	Show the application window after the server response
	 *	with the permissions for the current user
	 **/
	showApplication		: function(info,options){
		var me = this,
			app = options.app,
			win = this.desktop.windowMgr.createWindow(app),
			cfg;

		if(win){
			var arr = app.klass.split("."),
				appname = arr[0];

			cfg = Ext.decode(app.configurations);
			//ruta del archivo donde esta el controlador
			Ext.Loader.setPath(appname,IAEN.desktop.Constants.JS_PATH+appname);
			Ext.Loader.require(app.klass,function(){
				var controller,
					id = win.id+"-"+app.klass;
				me.desktop.add(win);
				me.desktop.windowMgr.loader.hide();
				
				if(cfg.singleton){
					controller = me.controllers.get(id);
				}
				
				if(!controller){
					controller = Ext.create(me.getModuleClassName(app.klass, 'controller'), {
						permissions	: info.data,
		                application	: me,
		                id			: id
		            });
					me.controllers.add(controller);
					controller.win = win;
					controller.init(me);
					controller.onLaunch(me);
					win.on("destroy",function(){
						me.destroyController(controller);
					});
				}
				
				win.show();
			});
			
		}else{
			me.showNotification({
				message	: "Error al cargar el módulo de escritorio! por favor , reporte este problema a la administración."
			});
		}
	},
	
	onPermissionsError	: function(data){
		me.showNotification(data);
	},
	
	destroyController	: function(controller){
		var me = this;
		
		//remove from collection
		me.controllers.remove(controller);
		for(var i=0,len=controller.selectors.length;i<len;i++){
			var obj = controller.selectors[i];
			for(var s in obj){
				for(var ev in obj[s]){
					//remove selectors from event bus
					delete me.eventbus.bus[ev][s];
				}
				
			}
		}
		delete controller;
	},
	
	/**
	 * This function allow you to display notifications in the desktop
	 * @param {Object} config The message to show
	 */
	showNotification: function(data){
		Ext.create("IAEN.desktop.Notification",{
			message	: data.message
		});
	},
	
	/**
	 * This function show the login form in the desktop
	 * @param {Object} config The message to show
	 */
	showLoginWindow	: function(data){
		Ext.require("IAEN.modules.login.LoginWindow",function(){
			var win = Ext.create("IAEN.modules.login.LoginWindow",{
				modal	: true,
				forward	: false
			});
			win.show();
		});
	},
	
	onError	: function(data){
		
		Ext.Msg.alert("Error!","Lo sentimos muchos , pero hubo un error al cargar su configuración inicial.");
	},
	
	onUnload : function(e) {
        if (this.fireEvent('beforeunload', this) === false) {
            e.stopEvent();
        }
    }
});