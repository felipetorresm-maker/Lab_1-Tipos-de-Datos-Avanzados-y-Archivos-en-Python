from json import dumps
from json import loads

def ingreso_usuario(id, nombre, apellido, contrasena, rol):
    archivo = "data.txt"
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            usuarios = file.readlines()
    except FileNotFoundError:
        usuarios = []   
    
    registro = {
        "identificacion": id,
        "nombre": nombre,
        "apellido": apellido,
        "contrasena": contrasena,
        "cargo": rol,
        "sesion_activa": False
    }

    for linea in usuarios:
        usuario_existente = loads(linea)
        
        if usuario_existente["identificacion"] == id:
            return "El usuario ya existe"
    
    usuarios.append(dumps(registro) + "\n")

    try:
        with open(archivo, "w", encoding="utf-8") as file:
            for linea in usuarios:
                file.write(linea)
    except:
        return "Error al guardar usuario"

    return "Registro exitoso"