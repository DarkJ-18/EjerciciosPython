#1 
# Crear clase Persona
class Persona:
    # Crear atributos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Crear métodos
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear clase Estudiante (Estudiante hereda lo que tiene Persona)
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"Soy {self.nombre} y estoy en {self.grado} grado.")

if __name__ == "__main__":
    # Crear objeto Persona 
    persona = Persona("Freddy", 40)
    persona.saludar()

    print("\n")
    # Crear objeto Estudiante 
    persona1 = Estudiante("Ana", 15, 10)
    persona1.saludar()
    persona1.mostrar_grado()


#2

class Calculadora:
    # Crear atributos
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def sumar(self):
        return self.numero1 + self.numero2
    
    def restar(self):
        return self.numero1 - self.numero2
    
    def multiplicar(self):
        return self.numero1 * self.numero2
    
    def dividir(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "Error: División por cero"

def main():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    
    calc = Calculadora(numero1, numero2)  # Crear objeto
    
    print("Suma:", calc.sumar())
    print("Resta:", calc.restar())
    print("Multiplicación:", calc.multiplicar())
    print("División:", calc.dividir())

if __name__ == "__main__":
    main()
#3
class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.historial = []

    def sumar(self):
        resultado = self.numero1 + self.numero2
        self.historial.append(f"Suma: {self.numero1} + {self.numero2} = {resultado}")
        return resultado
    
    def restar(self):
        resultado = self.numero1 - self.numero2
        self.historial.append(f"Resta: {self.numero1} - {self.numero2} = {resultado}")
        return resultado
    
    def multiplicar(self):
        resultado = self.numero1 * self.numero2
        self.historial.append(f"Multiplicación: {self.numero1} * {self.numero2} = {resultado}")
        return resultado
    
    def dividir(self):
        if self.numero2 != 0:
            resultado = self.numero1 / self.numero2
            self.historial.append(f"División: {self.numero1} / {self.numero2} = {resultado}")
            return resultado
        else:
            self.historial.append("División: Error - División por cero")
            return "Error: División por cero"
    
    def mostrar_historial(self):
        for operacion in self.historial:
            print(f" - {operacion}")

    def limpiar_historial(self):
        self.historial.clear()

# Borrar pantalla según sistema operativo
import os
def borrar_pantalla():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def main():
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Los valores deben ser números.")
        return

    calc = Calculadora(numero1, numero2)
    print("Suma:", calc.sumar())
    print("Resta:", calc.restar())
    print("Multiplicación:", calc.multiplicar())
    print("División:", calc.dividir())
    print("Historial:")
    calc.mostrar_historial()

if __name__ == "__main__":
    while True:
        borrar_pantalla()
        main()
        resp = input("Desea continuar (1 si - 0 no): ")
        if resp == '0':
            break


#4
import math

class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        return self.numero1 + self.numero2

    def restar(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "Error: División por cero"

class CalculadoraCientifica(Calculadora):
    def potencia(self):
        return self.numero1 ** self.numero2

    def raiz_cuadrada(self, numero):
        return math.sqrt(numero)

if __name__ == "__main__":
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    calc = CalculadoraCientifica(numero1, numero2)
    print("Suma:", calc.sumar())
    print("Resta:", calc.restar())
    print("Multiplicación:", calc.multiplicar())
    print("División:", calc.dividir())
    print("Potencia:", calc.potencia())
    print("Raíz Cuadrada del primer número:", calc.raiz_cuadrada(numero1))


#5

# Definición de la clase Empleado
class Empleado:
    # Método constructor que inicializa nombre y salario
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    # Método para mostrar los datos del empleado
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Salario: {self.salario}")

# Definición de la clase Gerente que hereda de Empleado
class Gerente(Empleado):
    # Método constructor que inicializa nombre, salario y departamento
    def __init__(self, nombre, salario, departamento):
        # Llama al constructor de la clase padre (Empleado) para inicializar nombre y salario
        super().__init__(nombre, salario)
        self.departamento = departamento

    # Método para mostrar los datos del gerente, incluyendo el departamento
    def mostrar_datos(self):
        # Llama al método mostrar_datos de la clase padre (Empleado)
        super().mostrar_datos()
        print(f"Departamento: {self.departamento}")

if __name__ == "__main__":
    # Creación de una instancia de Empleado
    empleado = Empleado("Carlos", 3000)
    # Creación de una instancia de Gerente
    gerente = Gerente("Ana", 5000, "Ventas")

    # Mostrar los datos del empleado
    empleado.mostrar_datos()
    print("\n")  # Salto de línea para separar la salida
    # Mostrar los datos del gerente
    gerente.mostrar_datos()



#6
# Definición de la clase Libro
class Libro:
    # Método constructor que inicializa título, autor y año del libro
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    # Método para mostrar la información del libro
    def mostrar_informacion(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}")

# Definición de la clase Biblioteca
class Biblioteca:
    # Método constructor que inicializa una lista vacía de libros
    def __init__(self):
        self.libros = []

    # Método para agregar un libro a la biblioteca
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Método para mostrar la información de todos los libros en la biblioteca
    def mostrar_libros(self):
        for libro in self.libros:
            libro.mostrar_informacion()

# Bloque principal del programa
if __name__ == "__main__":
    # Creación de instancias de Libro
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("Don Quijote", "Miguel de Cervantes", 1605)

    # Creación de una instancia de Biblioteca
    biblioteca = Biblioteca()
    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    
    # Mostrar la información de todos los libros en la biblioteca
    biblioteca.mostrar_libros()


#7
# Definición de la clase Producto
class Producto:
    # Método constructor que inicializa nombre, precio y cantidad del producto
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    # Método para mostrar la información del producto
    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")

# Definición de la clase Inventario
class Inventario:
    # Método constructor que inicializa una lista vacía de productos
    def __init__(self):
        self.productos = []

    # Método para agregar un producto al inventario
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método para mostrar la información de todos los productos en el inventario
    def mostrar_inventario(self):
        for producto in self.productos:
            producto.mostrar_informacion()

# Bloque principal del programa
if __name__ == "__main__":
    # Creación de instancias de Producto
    producto1 = Producto("Laptop", 1200, 10)
    producto2 = Producto("Mouse", 20, 50)

    # Creación de una instancia de Inventario
    inventario = Inventario()
    # Agregar productos al inventario
    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)

    # Mostrar la información de todos los productos en el inventario
    inventario.mostrar_inventario()


#8
# Definición de la clase Votante
class Votante:
    # Método constructor que inicializa el nombre y la edad del votante
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método para verificar si el votante puede votar
    def puede_votar(self):
        # Retorna True si la edad del votante es mayor o igual a 18, de lo contrario, False
        return self.edad >= 18

# Bloque principal del programa
if __name__ == "__main__":
    # Creación de instancias de Votante
    votante1 = Votante("Luis", 20)  # Votante mayor de edad
    votante2 = Votante("María", 16)  # Votante menor de edad

    # Verificación y muestra si los votantes pueden votar
    print(f"{votante1.nombre} puede votar: {votante1.puede_votar()}")  # Debería imprimir True
    print(f"{votante2.nombre} puede votar: {votante2.puede_votar()}")  # Debería imprimir False


#9
# Definición de la clase Reservación
class Reservacion:
    # Método constructor que inicializa nombre, fecha y hora de la reservación
    def __init__(self, nombre, fecha, hora):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora

    # Método para mostrar la información de la reservación
    def mostrar_reservacion(self):
        print(f"Reservación a nombre de {self.nombre} para el {self.fecha} a las {self.hora}")

# Definición de la clase SistemaReservaciones
class SistemaReservaciones:
    # Método constructor que inicializa una lista vacía de reservaciones
    def __init__(self):
        self.reservaciones = []

    # Método para agregar una reservación al sistema
    def agregar_reservacion(self, reservacion):
        self.reservaciones.append(reservacion)

    # Método para mostrar la información de todas las reservaciones en el sistema
    def mostrar_reservaciones(self):
        for reservacion in self.reservaciones:
            reservacion.mostrar_reservacion()

# Bloque principal del programa
if __name__ == "__main__":
    # Creación de instancias de Reservacion
    res1 = Reservacion("Ana", "2023-08-15", "18:00")
    res2 = Reservacion("Carlos", "2023-08-16", "20:00")

    # Creación de una instancia de SistemaReservaciones
    sistema = SistemaReservaciones()
    # Agregar reservaciones al sistema
    sistema.agregar_reservacion(res1)
    sistema.agregar_reservacion(res2)

    # Mostrar la información de todas las reservaciones


#10
# Definición de la clase Estudiante
class Estudiante:
    # Método constructor inicializa nombre del estudiante y una lista vacía para las notas
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    # Método para agregar una nota a la lista de notas del estudiante
    def agregar_nota(self, nota):
        self.notas.append(nota)

    # Método para calcular el promedio de las notas del estudiante
    def promedio(self):
        # Retorna el promedio de notas si la lista notas no está vacía, de lo contrario, retorna 0
        return sum(self.notas) / len(self.notas) if self.notas else 0

# Bloque principal del programa

