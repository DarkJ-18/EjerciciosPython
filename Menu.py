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