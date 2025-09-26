from funcion import ingreso_usuario
from funcion2 import inicio_sesion

while True:
    id = int(input("Ingrese su número de identificación: "))
    name = str(input("Ingrese su nombre: "))
    last_name = str(input("Ingrese su apellido: "))
    password = str(input("Ingrese su contraseña: "))
    rol = str(input("Ingrese su rol: "))

    usuarios = ingreso_usuario(id, name, last_name, password, rol)
    print(usuarios)

    u = input("¿Desea registrar otro usuario?: ")
    if u != "si":
        print("Cancelando registro de usuario")
        i = input("¿Desea iniciar sesión?: ")
        if i == "si":
            id = int(input("Ingrese su número de identificación: "))
            password = str(input("Ingrese su contraseña: "))
            resultado = inicio_sesion(id, password)
            print(resultado)
        break
