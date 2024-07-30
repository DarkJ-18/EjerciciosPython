#Ejercicio 3.- Escribe un programa en Python que realice las siguientes acciones:

    # 1. Inicialice una lista vacía llamada notas para almacenar las calificaciones de los estudiantes.
    # 2. Solicite al usuario que ingrese 10 notas. Cada nota debe ser un número decimal y se almacenará en la lista notas.
    # 3. Solicite al usuario que ingrese una nota específica que desea buscar en la lista de notas.
    # 4. Busque todas las posiciones en la lista notas donde se encuentra la nota especificada por el usuario y almacene estas posiciones en una lista llamada posiciones.
    # 5. Verifique si la nota especificada se encontró en la lista notas.
    # 6. Si se encontraron posiciones, imprima las posiciones (basadas en 1, no en 0) donde se encuentra la nota.
    # 7. Si la nota no se encontró en la lista notas, imprima un mensaje indicando que la nota no se encontró. 
    
notas =[]

for i in range(3):
    nota = float(input("Digite una nota "))
    notas.append(nota)
x = float(input("Digite una nota a buscar "))

posiciones = []
for i,n in enumerate(notas):
    if x == n:
        posiciones.append(x)

print(f"El numero {x} esta en estas posiciones {posiciones} ")
