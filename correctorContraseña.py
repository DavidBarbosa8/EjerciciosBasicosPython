txtUsuario = input ("Ingrese su contraseña, recuerde que debe contener 8 caracteres \n")

validacionContraseña = len(txtUsuario)

if(validacionContraseña == 0):
    print ("POr favor ingrese su contraseña")
elif (validacionContraseña < 8):
    print ("La contraseña no cumple con el requemiento minimo de caracteres")
elif (validacionContraseña == 8):
    print ("La contraseña es correcta y cumple con los requerimientos")
else : 
    print ("La contraseña es demasiado extensa y no cumple los requerimientos")    
