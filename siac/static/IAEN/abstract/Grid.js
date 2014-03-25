/**
 * @class IAEN.abstract.Grid
 * @extends Ext.grid.Panel
 * requires 
 *
 * Description
 *
 *
 **/

Ext.define("IAEN.abstract.Grid",{
	extend		: "Ext.grid.Panel",
	
	paging		: true,
	border		: false,
	full		: true,
	
	initComponent	: function() {
		var me = this;
		
		if(me.paging){
			me.dockedItems = [{
				xtype		: "pagingtoolbar",
				store		: me.store,
				dock		: "bottom",
				displayInfo	: true
		    }];
		}
		
        
		me.callParent();
	}
});