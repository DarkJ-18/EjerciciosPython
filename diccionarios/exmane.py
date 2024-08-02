libro = {}

def crearLibro():
    idl = input("Ingrese el id del libro: ")
    if idl in libro:
        print(f"Error: El libro con id {idl} ya existe.")
    else:
        nombre = input("Ingrese el nombre del libro: ")
        descripcion = input("Ingrese la descripcion: ")
        autor = input("Ingrese el autor: ")
        genero = input("Ingrese el genero del libro: ")
        
        libro[idl] = {"nombre": nombre, "descripcion": descripcion, "autor": autor, "genero": genero}
        print(f"Libro con id {idl} creado exitosamente.")

def leerLibro():   
    if libro:
        for idl, detalles in libro.items():
            print(f"id libro: {idl}, nombre: {detalles['nombre']}, descripcion: {detalles ['descripcion']}, autor: {detalles ['autor']}, genero: {detalles['genero']}")
    else:
        print("No hay libros en la biblioteca.")

def actualizarLibro():
    idl = input("Ingrese el id del libro a actualizar: ")
    if idl in libro:
        nombre = input("Ingrese el nuevo nombre del libro: ")
        descripcion = input("Ingrese la nueva descripcion: ")
        autor = input("Ingrese el nuevo autor: ")
        genero = input("Ingrese el nuevo genero del libro: ")
        
        if nombre:
            libro[idl]["nombre"] = nombre
        if descripcion:
            libro[idl]["descripcion"] = descripcion
        if autor:
            libro[idl]["autor"] = autor
        if genero:
            libro[idl]["genero"] = genero
        print(f"Libro con ID {idl} actualizado exitosamente.")
    else:
        print(f"Error: El libro con ID {idl} no existe.")
        
def eliminarLibro():
    idl = input("Ingrese el id del libro a eliminar: ")
    if idl in libro:
        del libro[idl]
        print(f"Libro con ID {idl} eliminado exitosamente.")
    else:
        print(f"Error: El libro con ID {idl} no existe.")
        
def mostrarMenu():
    print("\n--- Menú CRUD ---")
    print("1 / CREAR LIBRO")
    print("2 / LEER LIBRO")
    print("3 / ACTUALIZAR LIBRO")
    print("4 / ELIMINAR LIBRO")
    print("5 / SALIR")

if __name__ == "__main__":
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crearLibro()
        elif opcion == '2':
            leerLibro()
        elif opcion == '3':
            actualizarLibro()
        elif opcion == '4':
            eliminarLibro()
        elif opcion == '5':
                print("Saliendo...")
                print("Gracias por usar el programa :)...")
                break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")