# Diccionario de productos inicial
productos = {}

# Función para crear un nuevo producto
def crear_producto(cod, nombre, valor, cantidad):
    if cod in productos:
        print(f"Error: El producto con código {cod} ya existe.")
    else:
        productos[cod] = {"nombre": nombre, "valor": valor, "cantidad": cantidad}
        print(f"Producto {nombre} creado exitosamente.")

# Función para leer (mostrar) los detalles de un producto
def leer_producto(cod):
    if cod in productos:
        print(f"Detalles del producto {cod}: {productos[cod]}")
    else:
        print(f"Error: El producto con código {cod} no existe.")

# Función para actualizar un producto
def actualizar_producto(cod, nombre=None, valor=None, cantidad=None):
    if cod in productos:
        if nombre is not None:
            productos[cod]["nombre"] = nombre
        if valor is not None:
            productos[cod]["valor"] = valor
        if cantidad is not None:
            productos[cod]["cantidad"] = cantidad
        print(f"Producto {cod} actualizado exitosamente.")
    else:
        print(f"Error: El producto con código {cod} no existe.")

# Función para eliminar un producto
def eliminar_producto(cod):
    if cod in productos:
        del productos[cod]
        print(f"Producto {cod} eliminado exitosamente.")
    else:
        print(f"Error: El producto con código {cod} no existe.")

# Ejemplo de uso del CRUD

# Crear productos
crear_producto(1, "Manzanas", 0.5, 100)
crear_producto(2, "Naranjas", 0.3, 150)

# Leer productos
leer_producto(1)
leer_producto(2)

# Actualizar productos
actualizar_producto(1, valor=0.6, cantidad=120)

# Leer producto actualizado
leer_producto(1)

# Eliminar un producto
eliminar_producto(2)

# Intentar leer un producto eliminado
leer_producto(2)