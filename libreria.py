#funciones
#validamos edad
def validar_edad(edad):
    return edad >= 18

#validar que el nombre solo contenga letras
def validar_nombre(nombre):
    return nombre.isalpha()

#solo números y máximo largo 6 digitos
def validar_clave(clave):
    return clave.isdigit() and len(clave) <= 6

#para validar que exista en el diccionario
def validarUsuario(nombre):
    return nombre.isalpha()

#para validar que exista en el diccionario
def validarClave(clave):
    return clave.isdigit()



