#1
valor = None
print("El valor de la variable es:", valor)


#2
def funcion_sin_retorno():
    print("Esta función no devuelve nada")


resultado = funcion_sin_retorno()
print("El resultado de la función es:", resultado)

#3
def funcion_con_argumento(arg=None):
    if arg is None:
        print("No se proporcionó ningún argumento")
    else:
        print("El argumento es:", arg)

funcion_con_argumento()
funcion_con_argumento("Hola")




#4

while True:
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == 'n':
        break
print("El algoritmo ha finalizado.")


#5

for i in range(5):
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == 'n':
        break
    print("El algoritmo sigue ejecutándose...")
print("El algoritmo ha finalizado.")

#6
numeros = [1, 5, 8, 10, 15, 20, 25, 30]
limite = 12
numero_encontrado = None

for num in numeros:
    if num > limite:
        numero_encontrado = num
        break

if numero_encontrado is not None:
    print("El primer número mayor que", limite, "es:", numero_encontrado)
else:
    print("No se encontró ningún número mayor que", limite)


#7

import sys

def verificar_autenticacion(usuario_autenticado):
    if usuario_autenticado:
        print("Bienvenido")
    else:
        sys.exit("Error: El usuario no está autenticado")

verificar_autenticacion(False)
print("Esta línea no se ejecutará si el usuario no está autenticado")

#8

while True:
    opcion = input("Ingrese una opción (o escriba 'salir' para salir): ")
    if opcion.lower() == 'salir':
        print("Saliendo del script...")
        exit()
    else:
        print("Realizando la operación correspondiente a:", opcion)

#9
lista = [1, 2, None, 4, 5]
if None in lista:
    print("La lista contiene None")
else:
    print("La lista no contiene None")



#10
lista = [1, 2, None, 4, None, 5]
lista_filtrada = [x for x in lista if x is not None]
print("Lista sin elementos None:", lista_filtrada)


#11
lista = [1, 2, None, 4, None, 5]
contador = lista.count(None)
print("Número de elementos None en la lista:", contador)


#12
lista = [1, 2, 3, 4, 5]
elemento_buscado = 3

for elemento in lista:
    if elemento == elemento_buscado:
        print("Elemento encontrado:", elemento_buscado)
        break
else:
    print("Elemento no encontrado")


#13
lista_de_listas = [[1, 2, 3], [4, None, 6], [7, 8, 9]]

for sublista in lista_de_listas:
    if None in sublista:
        print("Sublista que contiene None:", sublista)
        break

#14
numeros = [2, 4, 6, 11, 14, 17, 20]

for num in numeros:
    if num % 2 == 0:
        print("Número par:", num)
        continue
    if num > 10:
        print("Número impar mayor que 10:", num)
        break

#15
def primer_elemento(lista):
    if not lista:
        return None
    return lista[0]

# main
resultado = primer_elemento([])
print("El resultado es:", resultado)

resultado = primer_elemento([1, 2, 3])
print("El primer elemento es:", resultado)



#16
frases = ["Hola mundo", "Python es genial", "Me gusta programar", "Adiós mundo"]
palabra_buscada = "Python"

for frase in frases:
    if palabra_buscada in frase:
        print("Frase encontrada:", frase)
        break
else:
    print("Palabra no encontrada en ninguna frase")


#17

import sys

def verificar_positivo(numero):
    if numero <= 0:
        sys.exit("Error: El número no es positivo")
    print("El número es positivo:", numero)

# main
verificar_positivo(-5)
print("Esta línea no se ejecutará si el número no es positivo")

#18

while True:
    numero = int(input("Ingrese un número: "))
    if numero > 100:
        print("Número mayor que 100. Saliendo del bucle.")
        break

#19

import sys

contraseña_correcta = "12345"
contraseña_ingresada = input("Ingrese la contraseña: ")

if contraseña_ingresada != contraseña_correcta:
    sys.exit("Error: Contraseña incorrecta")

print("Contraseña correcta. Bienvenido.")

#20

diccionario = {'a': 1, 'b': None, 'c': 2, 'd': None}
diccionario_limpio = {k: v for k, v in diccionario.items() if v is not None}
print("Diccionario sin valores None:", diccionario_limpio)

