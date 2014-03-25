/**
 * @class IAEN.desktop.TaskbarContainer
 * @extends Ext.toolbar.Toolbar
 *
 * This class contains the buttons in the bar
 *
 **/

Ext.define("IAEN.desktop.TaskbarContainer",{
	extend 			: "Ext.toolbar.Toolbar",

	flex			: 1,
	enableOverflow	: true,
	cls				: "IAEN-toolbar-container",
	items			: ["&#160;"]
});