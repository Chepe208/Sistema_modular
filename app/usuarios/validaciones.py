def validar_nombre(nombre: str) -> bool:
    """Lanza el ValueError si el nombre esta vacio o solo tiene espacios."""
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío o solo contener espacios.")
    return True

def validar_edad(edad: int) -> bool:
    """Lanza el ValueError si la edad no esta entre 0 y 120."""
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero.")
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    if edad > 120:
        raise ValueError("La edad no puede ser mayor a 120.")
    return True