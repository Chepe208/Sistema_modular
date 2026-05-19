from app.config.settings import APP_NAME, APP_VERSION, config
from app.usuarios.gestor import registrar_usuario, listar_usuarios, buscar_usuario
from app.usuarios.validaciones import validar_nombre, validar_edad

def mostrar_menu():
    print(f"\n {APP_NAME} v{APP_VERSION} ")
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Salir")
    return input("Seleccione una opción: ")

def main():
    print(f"Bienvenido a {APP_NAME}")
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            try:
                nombre = input("Nombre: ")
                edad_str = input("Edad: ")
                edad = int(edad_str)
                usuario = registrar_usuario(nombre, edad)
                print(f" Usuario registrado con ID {usuario['id']}")
            except ValueError as e:
                print(f" Error: {e}")
            except Exception as e:
                print(f" Error inesperado: {e}")
        
        elif opcion == "2":
            usuarios = listar_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                print("\nLista de usuarios:")
                for u in usuarios:
                    print(f"ID: {u['id']} | Nombre: {u['nombre']} | Edad: {u['edad']}")
        
        elif opcion == "3":
            termino = input("Ingrese nombre o parte a buscar: ")
            try:
                resultados = buscar_usuario(termino)
                if resultados:
                    print("\nResultados encontrados:")
                    for u in resultados:
                        print(f"ID: {u['id']} | Nombre: {u['nombre']} | Edad: {u['edad']}")
                else:
                    print("No se encontraron coincidencias.")
            except ValueError as e:
                print(f" Error: {e}")
        
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()