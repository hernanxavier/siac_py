/**
 * @class IAEN.core.Log
 * @extends Object
 *
 * Class for logging
 *
 **/

Ext.define("IAEN.core.Log",{
	extend 		: "Object",
	singleton	: true,

	log			: function(object){
		if(console){
			console.log(object);
		}
	}
});

IAEN.log = IAEN.core.Log.log;