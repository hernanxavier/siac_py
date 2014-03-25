/**
 * @class IAEN.desktop.Window
 * @extends Ext.window.Window
 * requires Ext.ux.statusbar.StatusBar
 *
 * Description
 *
 *
 **/

Ext.define("IAEN.desktop.Window",{
	extend		: "Ext.window.Window",
	requires		: ["Ext.ux.statusbar.StatusBar"],
	
	title			: "Default title application",
	stateful		: false,
    isWindow		: true,
    minimizable		: true,
    maximizable		: true,
	width			: IAEN.desktop.Constants.DEFAULT_WINDOW_WIDTH,
	height			: IAEN.desktop.Constants.DEFAULT_WINDOW_HEIGHT,
	layout			: "fit",
	//renderTo		: IAEN.App.desktop.body.dom,
	constrain		: true,
	bodyPadding		: 2,

	initComponent	: function() {
		var me = this;

		this.statusBar = Ext.create("Ext.ux.statusbar.StatusBar", {
			dock		: "bottom",
			defaultText	: "Ready"
		});
		
		this.dockedItems = [this.statusBar];
        
		me.callParent();
	},
	
	doClose 		: function ()  {
        this.doClose = Ext.emptyFn; // dblclick can call again...
        this.el.disableShadow();
        this.el.fadeOut({
            listeners: {
				scope	: this,
                afteranimate: function () {
                    this.destroy();
                }
            }
        });
    }
});