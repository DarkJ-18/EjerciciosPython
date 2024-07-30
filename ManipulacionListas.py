import math
#1. Sumar Elementos Pares Escribe un algoritmo que sume todos los elementos pares de una lista de números enteros.
print("------------------1----------------")
lista = [1, 2, 3, 4, 5, 6]
sumaPares = sum(num for num in lista if num % 2 == 0)
print("La suma de los elementos pares es:", sumaPares)


#Suma de impares y pares ejercicio 1 y 2 

lista = [1,2,3,4,5,6]
producto_impares = 1
for num in lista:
    if num % 2 != 0:
        producto_impares *= num
        sumaImpares = sum(num for num in lista if num % 2 != 0)   
        print("suma impares", sumaImpares)
    elif num % 2 == 0:
        sumPares = sum(num for num in lista if num % 2 == 0)
        print("Suma pares", sumPares)
        
    

#2. Producto de Elementos Impares Escribe un algoritmo que calcule el producto de todos los elementos impares de una lista de números enteros.
print("------------------2----------------")
lista = [1, 2, 3, 4, 5, 6]
producto_impares = 1
for num in lista:
    if num % 2 != 0:
        producto_impares *= num
print("El producto de los elementos impares es:", producto_impares)

#3  Encontrar Elementos Comunes EscsumPares = sum(num for num in lista if num = 0)ribe un algoritmo que encuentre los elementos comunes entre dos listas y los muestre.
print("------------------3----------------")
lista1 = [1,2,3,4,5]
lista2 = [4,5,6,7,8]

comunes = list(set(lista1) & set(lista2))
print("Los elementos comunes son:", comunes)

#MENU DE LOS 3 EJERCICIOS ANTERIORES

import os 
if os.name=="nt": #para windows
    os.system("cls")
else: #para linux
    os.system("clear")
while True:
    x = int(input("---Ingrese la opcion---\n1-Suma de pares\n2-Suma Pares e impares\n3-Calcular Impares\n4-Encuenta el comun\n5-Salir"))
    
    if x == 1: 
        print("------------------1----------------")
        lista = [1, 2, 3, 4, 5, 6]
        sumaPares = sum(num for num in lista if num % 2 == 0)
        print("La suma de los elementos pares es:", sumaPares)
    elif x == 2:
        lista = [1,2,3,4,5,6]
        producto_impares = 1
        for num in lista:
            if num % 2 != 0:
                producto_impares *= num
                sumaImpares = sum(num for num in lista if num % 2 != 0)   
                print("suma impares", sumaImpares)
            elif num % 2 == 0:
                sumPares = sum(num for num in lista if num % 2 == 0)
                print("Suma pares", sumPares)
    elif x == 3:
        print("------------------2----------------")
        lista = [1, 2, 3, 4, 5, 6]
        producto_impares = 1
        for num in lista:
            if num % 2 != 0:
                producto_impares *= num
        print("El producto de los elementos impares es:", producto_impares)
    elif x == 4:
        lista1 = [1,2,3,4,5]
        lista2 = [4,5,6,7,8]

        comunes = list(set(lista1) & set(lista2))
        print("Los elementos comunes son:", comunes)
    elif x == 4:
        print("Adios <3 ")
        break  

#4 Eliminar los Primeros N Elementos Escribe un algoritmo que elimine los primeros N elementos de una lista.
print("------------------4----------------")
lista = [1,2,3,4,5,6,7,8]
N =3 
lista = lista[N:]
print("Lista sin los primeros N elementos:", lista)


print("------------------5----------------")
#Crear una Lista con Elementos Elevados al Cubo Escribe un algoritmo que genere una lista donde cada elemento sea el cubo de los números del 1 al 10.

cubos = [num**3 for num in range(1,11)]
print("Lista con elementos elevados al cubo:", cubos)

print("------------------6----------------")

#Ordenar Lista de Palabras por Longitud Escribe un algoritmo que ordene una lista de palabras por su longitud.
palabras = ["python","es","un","lenguaje","de","programacion"]
palabras_ordenadas = sorted(palabras,key=len)
print("Palabras ordenadas por longitud:", palabras_ordenadas)

print("------------------7----------------")
#Remover Elementos Negativos Escribe un algoritmo que elimine todos los elementos negativos de una lista de números
lista=[1,-2,3,-4,5,-6]
listaPositiva = [num for num in lista if num >= 0]
print("Lista sin elementos negativos: ", listaPositiva)
print("------------------8----------------")
#Encontrar el Segundo Mayor Número Escribe un algoritmo que encuentre el segundo mayor número en una lista de números.
lista = [1,2,3,4,5]
mayor = max(lista)
listaSinMayor = [num for num in lista if num != mayor]
segundoMayor = max(listaSinMayor)
print("EL SEGUNDO MAYOR NUMERO ES: ", segundoMayor)


print("------------------9----------------")
#Intercalar Elementos de dos Listas Escribe un algoritmo que intercale los elementos de dos listas de igual longitud.

lista1 = [1,3,5]
lista2 = [2,4,6]
listaIntercalada = [None]*(len(lista1)+len(lista2))
listaIntercalada[::2] = lista1
listaIntercalada[1::2] = lista2
print("Lista intercalada: ", listaIntercalada)

print("------------------10----------------")
#Dividir una Lista en dos Partes 
# Escribe un algoritmo que divida una lista en dos partes iguales.
# Si la lista tiene un número impar de elementos, la primera parte debe tener un elemento más que la segunda.

lista1 = [1,2,3,4,5]
mitad = len(lista1)//2
if len(lista1) % 2 == 0:
    lista2 = lista1[mitad:]
    lista1 = lista1[:mitad]
print("Lista 1: ", lista1)
print("Lista 2: ", lista2)

print("------------------11----------------")
#Crear una Lista de Factoriales 
# Escribe un algoritmo que genere una lista de factoriales de los números del 1 al 5.
factoriales = [math.factorial(num) for num in range(1,6)]
print("Lista de factoriales: ", factoriales)

print("------------------12----------------")
#Filtrar Palabras que Contengan una Subcadena 
# Escribe un algoritmo que filtre una lista de palabras y devuelva 
# solo las palabras que contienen una subcadena específica.

palabras = ["hola","mundo","holanda","python","holistico"]
subcadena = "hol"
palabrasFiltradas = [palabra for palabra in palabras if subcadena in palabra]
print("Palabras que contienen la subcadena hol:", palabrasFiltradas)


print("------------------13----------------")
#Duplicar Elementos de una Lista 
#Escribe un algoritmo que duplique cada elemento de una lista de números.

lista= [1,2,3,4,5]
listaDuplicada = [num*2 for num in lista]
print("Lista con los elementod duplicados:", listaDuplicada)

lista = [1,2,3,4,5]
listaDuplicada=[]
for ele in lista:
    listaDuplicada.append(ele*2)
print(listaDuplicada)



print("------------------14----------------")
#Alternar Mayúsculas y Minúsculas en una Lista de Strings 
# Escribe un algoritmo que alterne mayúsculas y minúsculas en una lista de strings.

palabras = ["python", "es", "genial"]
palabrasAlteradas = [palabras.upper() if i % 2 == 0 else palabras.lower() for i, palabras in enumerate(palabras)]
print(palabrasAlteradas)

print("------------------15----------------")
#Crear una Lista de Números Primos 
# Escribe un algoritmo que genere una lista de números primos menores a 20.

primos = []

for num in range(2,20):
    esPrimo = True
    if num <= 1:
        esPrimo = False
    for i in range(2,num):
        if num % i == 0:
            esPrimo = False
            break
    if esPrimo:
        primos.append(num)

print("Lista de numeros primos menores a 20: ", primos)



print("------------------16----------------")
#Crear una Lista de Números Fibonacci 
# Escribe un algoritmo que genere una lista de los primeros 10 números de Fibonacci.

fibonacci = [0,1]
for i in range(2,10):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print("Lista de los primeros 10 numeros de Fibonacci: ", fibonacci)

print("------------------17----------------")

#Escribe un algoritmo que elimine los elementos en posiciones impares de una lista.

lista = [1,2,3,4,5,6,7,8]

listaPares = [num for i, num in enumerate(lista) if i % 2 == 0]
print("Lista sin elementos en posiciones impares", listaPares)


print("------------------18----------------")
#Escribe un algoritmo que genere una lista de los números del 1 al 5 elevados a la cuarta potencia.

potencias = [num**4 for num in range(1,6)]
print("lista de potencias a la cuarta:", potencias)

print("------------------19----------------")

#Escribe un algoritmo que invierta el orden de los elementos en una lista de strings.

palabras = ["python", "es", "genial"]
palabrasInvertidas = palabras[::-1]

print("------------------20----------------")