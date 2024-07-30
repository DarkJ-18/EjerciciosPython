#break es una palabra clave en Python que se usa para salir de un bucle prematuramente, 
# antes de completar su ciclo. Se utiliza principalmente en bucles while y for.

#Cuando se encuentra la instrucción break dentro de un bucle, 
# el control del programa sale inmediatamente del bucle y continúa con la siguiente línea de código después del bucle.

#Ten en cuenta que break sirve solo para salir de los ciclos y del switch (según caso) 
# pero como no existe en Python el switch solo se una para los ciclos.

#1
while True:
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == 'n':
        # Si la respuesta es 'n', salimos del bucle while
        break  
    
    # Aquí va el resto del código que se ejecutará mientras la respuesta no sea 'n'
    print("El algoritmo sigue ejecutándose...")

# Continuamos con el resto del código fuera del bucle
print("El algoritmo ha finalizado.")


#2
for i in range(5):
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == 'n':
        # Si la respuesta es 'n', salimos del bucle for
        break  
    
    # Aquí va el resto del código que se ejecutará mientras la respuesta no sea 'n'
    print("El algoritmo sigue ejecutándose...")

# Continuamos con el resto del código fuera del bucle
print("El algoritmo ha finalizado.")


#3
numeros = [1, 5, 8, 10, 15, 20, 25, 30]
limite = 12
numero_encontrado = None

for num in numeros:
    if num > limite:
        numero_encontrado = num
        # Salir del bucle una vez que se encuentra el primer número mayor que el límite
        break

if numero_encontrado is not None:
    print("El primer número mayor que", limite, "es:", numero_encontrado)
else:
    print("No se encontró ningún número mayor que", limite)
