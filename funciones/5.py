#Ejercicio 5.- Se te ha asignado la tarea de desarrollar un programa que cree y muestre los elementos de una matriz bidimensional 
# de dimensiones 4x5, es decir, 4 filas y 5 columnas. Cada elemento de la matriz
# debe ser un número entero generado aleatoriamente entre 1 y 100, inclusivo. Una vez generada, 
# la matriz debe ser mostrada en pantalla, elemento por elemento, 
# junto con sus índices correspondientes para facilitar su identificación.

mat = []

for i in range(4):
    fila = []
    for j in range(4):
        x = i
        fila.append(x)
    mat.append(fila)

for i in range(4):
    for j in range(4):
        print(f"Mat en la posicicon {i},{j} = {mat[i][j]} ")
    print("\n")