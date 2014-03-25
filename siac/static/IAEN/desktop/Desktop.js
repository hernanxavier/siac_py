/**
 * @class IAEN.desktop.Desktop
 * @extends Ext.panel.Panel
 * requires IAEN.desktop.TaskBar
 *
 * The desktop class
 *
 *
 **/

Ext.define("IAEN.desktop.Desktop",{
	extend		: "Ext.panel.Panel",
	alias		: "widget.desktop",
	requires	: [
		"IAEN.desktop.Taskbar",
		"IAEN.desktop.Shortcuts",
		"IAEN.desktop.Wallpaper",
		"IAEN.desktop.FitAllLayout"
	],
	
	id			: "IAEN-desktop",
	border		: false,
	layout		: "fitall",

	initComponent	: function() {
		var me = this;

		me.taskbar = Ext.create("IAEN.desktop.Taskbar",me.userConfig);
		me.dockedItems = [me.taskbar];
		me.windowMgr = Ext.create("IAEN.desktop.WindowManager",{taskbar:me.taskbar});
	
		me.shortcuts = Ext.create("IAEN.desktop.Shortcuts",{
			applications	: me.userConfig.applications
		});
		
		me.wallpaper = Ext.create("IAEN.desktop.Wallpaper",{
			wallpaper	: IAEN.BASE_PATH+me.userConfig.config.wallpaper
		});
		
		
		
		me.windowMenu = new Ext.menu.Menu(me.createWindowMenu());

		me.items = [
			me.wallpaper,//esto va primero pero oculta el grupo de iconos
		    me.shortcuts,//este va segundo
		];
        
		me.callParent();
		
		me.shortcuts.on("itemclick", me.onShortcutItemClick, me);
		IAEN.Ajax.on("sessionexpired",IAEN.App.showLoginWindow,IAEN.App);
		IAEN.Ajax.on("showerror",IAEN.App.showNotification,IAEN.App);
	},
	
	createWindowMenu: function () {
        var me = this;
        return {
            defaultAlign: 'br-tr',
            items: [
                { text: 'Restore', handler: me.windowMgr.onWindowMenuRestore, scope: me.windowMgr },
                { text: 'Minimize', handler: me.windowMgr.onWindowMenuMinimize, scope: me.windowMgr },
                { text: 'Maximize', handler: me.windowMgr.onWindowMenuMaximize, scope: me.windowMgr },
                '-',
                { text: 'Close', handler: me.windowMgr.onWindowMenuClose, scope: me }
            ],
            listeners: {
                beforeshow	: me.windowMgr.onWindowMenuBeforeShow,
                hide		: me.windowMgr.onWindowMenuHide,
                scope		: me.windowMgr
            }
        };
    },

	onShortcutItemClick	: function(dataview,record,el,index,event){
		IAEN.App.runApplication({
			initialConfig : record.data
		});
	}
});