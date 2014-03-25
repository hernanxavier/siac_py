/**
 * @class IAEN.desktop.Shortcuts
 * @extends Ext.view.View
 * requires 
 *
 * Description
 *
 *
 **/

Ext.define("IAEN.desktop.Shortcuts",{
	extend		: "Ext.view.View",
	cls			: "IAEN-shortcuts-view",
	overItemCls	: "IAEN-shortcut-over",
    trackOver	: true,
    itemSelector: "div.IAEN-shortcut",
	config		: {
		iconWidth	: 48 //48,
	},

	/**
     * @cfg {String} shortcutTpl
     * This XTemplate is used to render items in the DataView. If this is changed, the
     * {@link shortcutItemSelect} will probably also need to changed.
     */
    shortcutTpl: [
		'<div class="IAEN-shorcuts-container">',
        '<tpl for=".">',
            '<div class="IAEN-shortcut">',
                '<div  class="IAEN-shortcut-icon {iconCls}">',//roles-app-shorcut-icon {iconCls}
                    '<img src="'+Ext.BLANK_IMAGE_URL+'" title="{text}">', //"',Ext.BLANK_IMAGE_URL,'" {text}
                '</div>',
                '<span class="IAEN-shortcut-text">{text}</span>',//{text}
            '</div>',
        '</tpl>',
        '</div>',
        '<div class="x-clear"></div>'
    ],

	initComponent	: function() {
		var me = this;
		
		me.store = Ext.create("Ext.data.ArrayStore",{
			fields	: ["text","class","iconCls"]
		});
		me.getShorcuts(me.applications);
        me.tpl = new Ext.XTemplate(me.shortcutTpl);

		me.initConfig(arguments);
		console.log("argumetns shorctus wilf ");
		me.callParent();
		
		me.on("resize",me.refreshView,me);
		
	},
	
	getShorcuts	: function(applications){
		if(applications){
			Ext.each(applications,function(app){
				
				if(app.menu){
					this.getShorcuts(app.menu);
				}else{
					if(app.configurations){
						var config = Ext.decode(app.configurations);
						
						if(config && config.shorcutIconCls){
							app.iconCls = config.shorcutIconCls;
							console.log("wilfin final-> "+app.iconCls);
							this.store.add(app);
						}
					}
				}
			},this);
		}
	},
	
	refreshView				: function(){
		var me = this,
			container = me.el.select(".IAEN-shorcuts-container").first();

		if(container){
			container.setWidth((me.getIconWidth() + 60) * me.calculateColumns());
		}
	},
	
	calculateColumns	: function(){
		var me = this,
			total = me.store.getCount(),
			shortcut = me.el.select(".IAEN-shortcut").first();
			itemsPerColumn = 0; 
			
		if(shortcut){
			itemsPerColumn = Math.floor(me.el.getHeight()/(shortcut.getHeight()+20));
		}	
			

		return itemsPerColumn > 0 ? Math.ceil(total/itemsPerColumn):itemsPerColumn;	
	}
});