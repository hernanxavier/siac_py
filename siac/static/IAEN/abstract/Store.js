/**
 * @class IAEN.abstract.Store
 * @extends Ext.data.Store
 * requires 
 *
 * Description
 *
 *
 **/

Ext.define("IAEN.abstract.Store",{
	extend	: "Ext.data.Store",
	
	autoLoad	: true,
	
	constructor	: function(options){
		var me = this;
		
		Ext.apply(me,options || {});
		me.proxy = {
	       type		: "ajax",
	       url		:  me.url,
	       reader	: {
	           	type			: "json",
	           	root			: "data",
	           	successProperty	: "success",
				totalProperty	: "total"
	       }
	   };
	
		me.callParent(arguments);
	}
});