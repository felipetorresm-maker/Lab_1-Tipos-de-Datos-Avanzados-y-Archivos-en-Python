from json import loads
from json import dumps

def inicio_sesion(id, password):
    archivo = "data.txt"

    try:
        with open(archivo, "r", encoding="utf-8") as file:
            usuarios = file.readlines()
    except FileNotFoundError:
        return "No hay usuarios registrados"

    nuevos_usuarios = []
    sesion_iniciada = False

    for u in usuarios:
        a = loads(u)

        if a["identificacion"] == id:
            if a["contrasena"] == password:
                a["sesion_activa"] = True
                sesion_iniciada = True
            else:
                return "Contraseña incorrecta"

        nuevos_usuarios.append(dumps(a) + "\n")

    
    with open(archivo, "w", encoding="utf-8") as file:
        for u in nuevos_usuarios:
            file.write(u)

    if sesion_iniciada:
        print("Inicio de sesión exitoso")
        return "Sesion activa"
    else:
        return "Usuario no encontrado"
