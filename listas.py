# 1. Crear una lista
lista= [1,2,3,4,5]
print(lista)

# 2. Imprimir un numero de la lista
print(lista[3])

# 3. Modificar el numero 1
lista[1]=10
print(lista)

# 4. Agregar un nuevo campo a la lista
lista.append(6)
print(lista)

# 5. Eliminar un elemento por valor
buscar=10
lista.remove(buscar)
print(lista)

# 6. Eliminar un elemento por indice
i=0
del lista[0]
print(lista)

# 7. Longitud de la lista
print(len(lista))

# 8. Extender la lista
lista.extend([7,8,9])
print(lista)

# 9. Insertar un elemento
lista.insert(0,0)
print(lista)

# 10. Limpiar la lista
lista.clear()
print(lista)

# 11. Revertir la lista
lista=[1,2,3,4,5]
lista.reverse()
print(lista)

# 12. Ordenar la lista
lista.sort()
print(lista)

#Ordenar la lista en reversa
lista.sort(reverse=True)
print(lista)

# 13. Índice de un Elemento
print(lista.index(4))

#14  Último Elemento con pop()
#Muestra y elimina el último elemento de la lista usando `pop()`, 
# y luego muestra la lista modificada.
ultimo = lista.pop()
print(ultimo)
print(lista)

#15.  Crear Lista de Listas
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista_de_listas)

#16. Acceder a Elementos de Sublistas
print(lista_de_listas[0][0])

#17. Añadir Sublista
#Añade una nueva sublista `[10, 11, 12]` usando `append()` y muestra la lista de listas.
lista_de_listas.append([10, 11, 12])
print(lista_de_listas)

#18. Fusionar dos Listas en Una Nueva Lista
print("---")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1)

#19 Lista de Strings
#Crea una lista de strings con los nombres de cinco 
#frutas y usa sort() para ordenarlos alfabéticamente.
frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]
frutas.sort()
print(frutas)

#20. Eliminar Elemento Específico Usando pop()
#Elimina el segundo elemento de la lista de frutas usando pop() 
# y muestra la lista modificada y el elemento eliminado.

elemento_eliminado = frutas.pop(1)
print(elemento_eliminado)
print(frutas)

#21. Eliminar todo el contenido de una lista clear()
lista.clear()
print(lista)




