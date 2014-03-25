/**
 * @class IAEN.modules.login.LoginForm
 * @extends IAEN.ui.Form
 *
 * Description
 *
 **/

Ext.define("IAEN.modules.login.LoginForm",{
	extend 			: "IAEN.abstract.Form",
	alias			: "loginform",
	forward			: true,
	initComponent	: function() {
		this.items = this.crearFormulario();
		this.callParent();
	},
	crearFormulario	: function(){
		return [{
			xtype	: "tabpanel",
			activeTab: 0,
			defaults : {
					bodyPadding : 10,
					layout : 'anchor'
				},
			items:[
				        { //tab login
				    	   title:'Login', 
				    	   //defaultType: 'textfield',
			                defaults: {
			                    anchor: '100%'
			                },//dentro de tablogin agregamos cajas de texto y un boton para ejecutar el ajax.
			                items: [{
			                	    xtype		:"textfield",
			        				labelAlign	: "left",
			        				msgTarget	: 'side',
			        				fieldLabel	: "Usuario",
			        				name		: "username",
			        				allowBlank	: false,
			        				flex		: 1,
			        				margins		: {right:3},
			        				maxLength  : 10,
					        		enforceMaxLength :10
			        			   },
			        			   {
			        				    xtype		:"textfield",
			        					labelAlign	: "left",
			        					msgTarget	: 'side',
			        					inputType	: 'password',
			        					fieldLabel	: 'Contraseña',
			        					name		: 'password',
			        					allowBlank	: false,
			        					flex		: 1,
			        					margins		: {left:3},
			        					maxLength  : 10,
						        		enforceMaxLength :10,
			        					listeners	: {
			        						scope		: this,
			        						specialkey	: function(f,e){
			        							if (e.getKey() == e.ENTER) {
			        								this.login();
			        							}
			        						}
			        					}
			        				},{
			        					xtype: 'button',
			        					anchor:  '40%',
			        					labelAlign : 'center',
			        					text: 'Loguearte',
			        					scope		: this,
			        					handler	: this.login
			        				}
			        				
			        			   ]
				        },//tab registrar
				        {
				    	    title:'Registrar',  
			                defaults: {
			                    anchor: '100%'
			                },
			                items:[{
				                	xtype		:"textfield",
			        				labelAlign	: "left",
			        				msgTarget	: 'side',
			        				fieldLabel	: "Nombre",
			        				name		: "txt_nombre",
			        				allowBlank	: false,
			        				flex		: 1,
			        				margins		: {right:3},
			        				maxLength   : 50,
			        				enforceMaxLength :50
			                	  },{
			                		 xtype		:"textfield",
				        		     labelAlign	: "left",
				        			 msgTarget	: 'side',
				        			 fieldLabel	: "Apellido",
				        			 name		: "txt_apellido",
				        			 allowBlank	: false,
				        			 flex		: 1,
				        			 margins	: {right:3},
				        			 maxLength  : 50,
				        			 enforceMaxLength :50
			                	  },{
			                		  xtype		:"textfield",
					        		  labelAlign	: "left",
					        		  msgTarget	: 'side',
					        		  fieldLabel	: "Correo",
					        		  name		: "txt_correo",
					        		  vtype:'email',
					        		  allowBlank	: false,
					        		  flex		: 1,
					        		  margins		: {right:3},
					        		  maxLength  : 50,
					        		  enforceMaxLength :50
			                	  },
			                	  {
			                		  xtype		:"textfield",
					        		  labelAlign	: "left",
					        		  msgTarget	: 'side',
					        		  fieldLabel	: "Usuario",
					        		  name		: "txt_usuario",
					        		  allowBlank	: false,
					        		  flex		: 1,
					        		  margins		: {right:3},
					        		  maxLength  : 10,
					        		  enforceMaxLength :10
			                	  },
			                	  {
			                		  xtype		:"textfield",
					        		  labelAlign: "left",
					        		  msgTarget	: 'side',
					        		  fieldLabel: "Clave",
					        		  name		: "txt_clave1",
					        		  inputType	: 'password',
					        		  allowBlank: false,
					        		  flex		: 1,
					        		  margins	: {right:3}	,
					        		  maxLength  : 10,
					        		  enforceMaxLength :10
			                	  },{
			                		  xtype		:"textfield",
					        		  labelAlign: "left",
					        		  msgTarget	: 'side',
					        		  fieldLabel: "Repita la clave",
					        		  name		: "txt_clave2",
					        		  inputType	: 'password',
					        		  allowBlank: false,
					        		  flex		: 1,
					        		  margins	: {right:3},
					        		  maxLength  : 10,
					        		  enforceMaxLength :10,
					        		  enableKeyEvents: true,
					        		  listeners: {
					        		        keyup: function(form, e) {
					        		        	var clave1 = this.previousSibling('[name=txt_clave1]');
					        		        	if(clave1.getValue() == this.getValue()){
					        		        		this.clearInvalid();
					        		        	}else{
					        		        		this.markInvalid('Las claves no concuerdan.');
					        		        	}
					        		          
					        		        }
					        		    }
			                	  },{
			                		   xtype	: 'button',
			        				   text		: 'Registrarse',
			        				   scope	: this,
			        				   handler	: this.registrar  
			                	    }
			                	  ]
				        }
			       ]
		
		}];
	},
	login		: function(){
		var valores = this.getForm().getValues();
		if(valores.username!='' && valores.password!='' ){
			 IAEN.Ajax.request({
				url		: IAEN.desktop.Constants.DESKTOP_LOGIN_URL,
				params	: valores,
				el		: this.up("window").el,
				scope	: this,
				success	: this.onSuccess,
				failure	: this.onFailure
			 });
		}else{
			Ext.Msg.alert("IAEN informa:","El usuario y la contraseña no deben estar vacios.");
		}
		 
	},
	registrar	:function(){
		var valores = this.getForm().getValues();
		var correo = this.down("textfield[name=txt_correo]");
		var usuario= this.down("textfield[name=txt_usuario]");
		var nombre= this.down("textfield[name=txt_nombre]");
		var apellido= this.down("textfield[name=txt_apellido]");
		var clave= this.down("textfield[name=txt_clave2]");
		
	
		if(correo.isValid() && correo.isValid() && usuario.isValid() && nombre.isValid() && apellido.isValid() && clave.isValid()){
			if(valores.txt_clave1 != valores.txt_clave2)
				Ext.Msg.alert("IAEN informa:","Las claves son incorrectas.");
			else{
				 IAEN.Ajax.request({
						url		: IAEN.desktop.Constants.DESKTOP_REGISTRAR_URL,
						params	: valores,
						el		: this.up("window").el,
						scope	: this,
						success	: this.onSuccess,
						failure	: this.onFailure
				  });
				 this.getForm().reset(); //limpia todos los campos del formulario.
			}
		}else{
			Ext.Msg.alert("IAEN informa:","Verifique los campos.");
		}
	},
	onSuccess	: function(data,response){
		if(data.success){
			if(this.forward){
				//envia al escritorio online
				if(data.url!='')
				  document.location = IAEN.desktop.Constants.DESKTOP_HOME_URL;
				else
				  Ext.Msg.alert("IAEN informa:",data.message);
				//Ext.Msg.alert("IAEN informa:",data.message);
			}else{
				var win = this.up("window");
				if(win){
					win.close();
				}
			}
			
		}
	},
	onFailure	: function(data,response){
		var passwrd = this.down("textfield[name=password]");

		Ext.create("Ext.tip.ToolTip",{
			anchor		: "left",
			target		: passwrd.bodyEl,
			trackMouse	: false,
			html		: data.message,
			autoShow	: true
		});
		Ext.Msg.alert("IAEN informa:",data.message);
		passwrd.markInvalid(data.message);
	}
});
