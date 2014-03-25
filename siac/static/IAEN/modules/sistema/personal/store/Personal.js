/**
 * @class CRM.sistema.personal.store.Personal
 * @extends Bleext.abstract.Store
 * requires 
 * @autor Wilfredo Marte S.
 * @date Lunes 24 de marzo del 2014. 
 *
 * Description
 *
 *
 **/

Ext.define("IAEN.modules.sistema.personal.store.Personal",{
	extend		: "IAEN.abstract.Store",
	model		: "IAEN.modules.sistema.personal.model.Personal",
	url			: "sistema/listar_personal/"
	
});

/*Ext.define('IAEN.modules.sistema.personal.store.Personal', {
    extend: 'IAEN.abstract.Store',
    model: 'IAEN.modules.sistema.personal.model.Personal',
    autoLoad: true,
    pageSize: 10,
    autoLoad: {start: 0, limit: 10},
    proxy: {
        type: 'ajax',
        api: {
            create: 'sistema/crear_personal/',
            read: 'sistema/listar_personal/',
            update: 'sistema/actualizar_personal/',
            destroy: 'sistema/eliminar_personal/',
        },
        reader: {
            type: 'json',
            root: 'Personal',
            successProperty: 'success'
        },
        writer: {
            type: 'json',
            writeAllFields: true,
            encode: true,
            root: 'Personal'
        }
    }
});*/