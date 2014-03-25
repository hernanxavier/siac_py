/**
 * @class IAEN.desktop.TaskBar
 * @extends Ext.Component
 *
 * Class for the Taskbar
 *
 **/

Ext.define("IAEN.desktop.Taskbar",{
	extend 			: "Ext.toolbar.Toolbar",
	requires		: [
		"IAEN.desktop.StartMenu",
		"IAEN.desktop.StartButton"
	],
	quickStart		: [],
	
	initComponent	: function () {
        var me = this;

		me.items = this.buildItems();
		me.dock='bottom';//agrega debajo el menu : bottom
		me.callParent();
    },

	buildItems		: function(){
		var me = this,
			sppliter = {
				xtype	: "splitter", html: "&#160;",
				height	: 20, width: 20, // TODO - there should be a CSS way here he:14
				cls		: "x-toolbar-separator x-toolbar-separator-horizontal IAEN-toolbar-splitter",
            };

		me.startMenu = Ext.create("IAEN.desktop.StartMenu",{
			applications	: me.applications,
			user			: me.user,
			position		: me.dock, //me.dock, bottom
		});

		me.startButton = Ext.create("IAEN.desktop.StartButton",{
			menu		: me.startMenu,
		});
		
       
		me.quickStart = Ext.create("Ext.toolbar.Toolbar",this.getQuickStart());
		me.windowBar = Ext.create("IAEN.desktop.TaskbarContainer");
		
		return [
			me.startButton,
			me.quickStart,
			sppliter,
			me.windowBar
		];
	},
	
	/**
     * This method returns the configuration object for the Quick Start toolbar. A derived
     * class can override this method, call the base version to build the config and
     * then modify the returned object before returning it.
     */
    getQuickStart	: function () {
		var me = this, ret = {
			minWidth		: 20,
			width			: 60,//60
			enableOverflow	: true,
			cls				: "IAEN-toolbar-container",
			items			: [
				{overflowText:"Hoja de Vida",tooltip:{ text: "Hoja de Vida", align: 'bl-tl' },iconCls:"IAEN-desktop-icon"}
			]
        };

        Ext.each(this.quickStart, function (item) {
			Ext.applyIf(item,{
				tooltip		: { text: item.text, align: 'bl-tl' },
				overflowText: item.text,
				iconCls		: "IAEN-default-quickstart-icon",
				scope		: IAEN.App,
				handler		: IAEN.App.runApplication
			});
        });

        return ret;
    },
	addTaskButton	: function(win) {
        var config = {
			cls			: "IAEN-toolbar-button",
            iconCls		: win.iconCls,
            enableToggle: true,
            toggleGroup	: 'all',
            width		: 120,
            text		: Ext.util.Format.ellipsis(win.title, 20),
            listeners	: {
                click: this.onWindowBtnClick,
                scope: this
            },
            win			: win
        };

        var cmp = this.windowBar.add(config);
        cmp.toggle(true);
        return cmp;
    },

	removeTaskButton: function (btn) {
        var found, me = this;
        me.windowBar.items.each(function (item) {
            if (item === btn) {
                found = item;
            }
            return !found;
        });
        if (found) {
            me.windowBar.remove(found);
        }
        return found;
    },

	onWindowBtnClick	: function(btn){
		var win = btn.win;

        if (win.minimized || win.hidden) {
            win.show();
        } else if (win.active) {
            win.minimize();
        } else {
            win.toFront();
        }
	},
	
	setActiveButton: function(btn) {
        if (btn) {
            btn.toggle(true);
        } else {
            this.windowBar.items.each(function (item) {
                if (item.isButton) {
                    item.toggle(false);
                }
            });
        }
    }
});