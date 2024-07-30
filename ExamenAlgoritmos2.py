print("MENU OPCIONES\n")

while True:
    x = int(input("Ingresa Numero:\n1--Sumar Lista\n2--Producto Lista\n3--Contar 3\n4--Maximo y Minimo\n5--Sin Duplicados\n6--Cambio Posicion\n7--Invertir Sublista\n8--Pares e Impares\n9--Join\n10--Numero Mayor\n11--Suma Sublista\n12--Promedio\n13--Pares\n14--Al cuadrado\n15--Si existe?\n16--lista negativos\n17--Concatenar\n18--Pares tuplas\n19--Lista Primeros 5 Naturales\n20--Palabras Mayusculas\n21--Salir \n"))
    
    if x == 1:
        print("---------1----------")
        lista = [1, 2, 3, 4, 5]
        print(sum(lista))
    elif x == 2:
        #2
        print("---------2----------")
        producto = 1
        for numero in lista:
            producto = producto * numero
        print(producto)
    elif x == 3:
        # 3 
        print("--------3----------")
        lista = [1, 2, 3, 4, 5, 3, 3]
        x= lista.count(3)
        print(x)
    elif x == 4:         
        #4
        print("--------4----------")
        lista = [1, 2, 3, 4, 5]
        maxi= max(lista)
        mini = min(lista)
        print(maxi)
        print(mini)
    elif x == 5:
        #5
        print("--------5----------")
        lista = [1, 2, 3, 4, 5, 3, 3]
        dupli = list(set(lista))
        print(dupli)
    elif x == 6:
        #6
        print("--------6----------")
        lista = [1, 2, 3, 4, 5]
        interca = lista[0], lista[-1] = lista[-1], lista[0]
        print(lista)
    elif x == 7:    
        #7
        print("--------7----------")
        lista = [1, 2, 3, 4, 5]
        print(lista)
        sublista = lista[1:4]
        sublista.reverse()
        lista[1:4] = sublista
        print(lista)
    elif x == 8:
        #8
        print("--------8---------")
        lista = [1, 2, 3, 4, 5]
        pares = len([num for num in lista if num % 2 == 0])
        impares = len([num for num in lista if num % 2 != 0])
        print("Pares")
        print(pares)
        print("Impares")
        print(impares)
    elif x == 9:
        #9
        print("--------9---------")
        frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]
        print("".join(frutas))
    elif x == 10:
        #10
        print("--------10---------")
        lista = [1, 2, 3, 4, 5]
        print([num for num in lista if num > 3])
    elif x == 11:               
        #11
        print("--------11---------")
        lista = [1, 2, 3, 4, 5]
        print(sum(lista[1:4]))
    elif x == 12:
        #12
        print("--------12---------")
        lista = [1, 2, 3, 4, 5]
        print(sum(lista) / len(lista))
    elif x == 13:        
        #13
        print("--------13---------")
        lista = [1, 2, 3, 4, 5]
        print([num for num in lista if num % 2 == 0])
    elif x == 14:
        #14
        print("--------14---------")
        print([num**2 for num in range(1, 6)])
    elif x == 15:
        #15
        print("--------15---------")
        lista = [1, 2, 3, 4, 5]
        print(3 in lista)
    elif x == 16:            
        #16
        print("--------16---------")
        print([-num for num in range(1, 11)])
    elif x == 17:    
        #17
        print("--------17---------")
        lista1 = [1, 2, 3]
        lista2 = [4, 5, 6]
        print(lista1+lista2)
    elif x == 18:
    #18
        print("--------18---------")
        lista1 = [1, 2, 3]
        lista2 = ["a", "b", "c"]
        print(list(zip(lista1, lista2)))
    elif x == 19:        
        #19
        print("--------19---------")
        print(list(range(1, 6)))
    elif x == 20:    
        #20
        print("--------20---------")
        palabras = ["HoLa", "MUNDO", "pYThon"]
        print([palabra.upper() for palabra in palabras])
    elif x == 21:
        print("Adios <3 ")
        break  