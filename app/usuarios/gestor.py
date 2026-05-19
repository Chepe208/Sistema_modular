from .validaciones import validar_nombre, validar_edad

usuarios_db = []
contador_id = 1

def registrar_usuario(nombre: str, edad: int) -> dict:
    global contador_id

    validar_nombre(nombre)
    validar_edad(edad)

    usuario = {
        "id": contador_id,
        "nombre": nombre.strip(),
        "edad": edad
    }
    usuarios_db.append(usuario)
    contador_id += 1
    return usuario

def listar_usuarios() -> list:
    return usuarios_db.copy()

def buscar_usuario(termino: str) -> list:
    """Busca usuarios por concidencia parcial en el nombre, devolviendo una lista de coincidencias."""
    termino = termino.strip().lower()
    if not termino:
        raise ValueError("El término de búsqueda no puede estar vacío.")
    resultados = [
        u for u in usuarios_db
        if termino in u["nombre"].lower()
    ]
    return resultados

def obtener_usuario_por_id(uid: int) -> dict:
    for u in usuarios_db:
        if u["id"] == uid:
            return u
    raise ValueError(f"Usuario con ID {uid} no encontrado.")