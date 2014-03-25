/**
 * @class IAEN.ui.ModalPanel
 * @extends Ext.Panel
 *
 * A modal panel that appears in top of everything
 *
 **/

Ext.define("IAEN.abstract.ModalWindow",{
	extend 			: "Ext.Window",
	
	layout			: "fit",
	cls				: "IAEN-window",
	modal			: true,
	draggable 		: false,
	resizable		: false,
	bodyPadding		: 10
});