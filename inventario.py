print("-----Sistema De Inventario------")
producto=[]
cantidad=[]
precio=[]
i = True
while i:
    x = int(input("\nIngresa Una Opcion\n1--CrearProducto\n2--Buscar Producto\n3--Eliminar Producto\n4--Actualizar Producto\n6--Organizar Inventario\n7--Invertir Inventario\n8--Borrar Inventario\n5--Salir\n"))
    if x == 1:
        apro = input("Ingresa El Nombrep Del Producto: ").capitalize()
        acan = int(input("Ingresa La Cantidad Del Producto: "))
        apre = int(input("Ingresa Precio Del Producto: "))
        producto.append(apro)
        cantidad.append(acan)
        precio.append(apre)
        print("\n-----Producto Almacenado Correctamente:)-----")
    elif x == 2:
        busPro = input("Ingresa Producto A Buscar: ").capitalize()
        resultado = busPro in producto
        if resultado:
            print("-----Producto Encontrado:)-----")
            elemento = producto.index(busPro)
            print("Nombre del Producto:", producto[elemento])
            print("Cantidad Del Producto:", cantidad[elemento])
            print("Precio Del Producto:", precio[elemento])
            print("-----Busqueda Finalizada:)-----\n")
        else:
            print("-----Producto No Encontrado -----\n")
            print("-----Busqueda Finalizada-----\n")
    elif x == 3:
        busPro = input("Ingresa El Producto A Eliminar: ").capitalize()
        resultado = busPro in producto
        if resultado:
            print("-----Producto Encontrado:)-----")
            elemento = producto.index(busPro)
            del producto[elemento]
            del cantidad[elemento]
            del precio[elemento]
            print("-----Producto Eliminado Correctamente -----")
        else:
            print("-----Producto No Encontrado -----")
    elif x == 4:
        busPro = input("Ingresa Producto A Actualizar: ").capitalize()
        resultado = busPro in producto
        if resultado:
            print("-----Producto Encontrado-----")
            npro = input("Ingresa El Nuevo Nombre Del Producto: ").capitalize()
            ncan = int(input("Ingresa La Nueva Cantidad Del Producto: "))
            npre = int(input("Ingresa El Nuevo Precio Del Producto: "))
            elemento = producto.index(busPro)
            producto[elemento] = npro
            cantidad[elemento] = ncan
            precio[elemento] = npre
            print("-----Producto Actualizado Correctamente -----")
        else:
            print("-----Producto No Encontrado :c")
    elif x == 5:
        print("----------Mostrar Todos Los Productos Del Inventario----------------")
        for i in producto:
            print(i)
        print("-----Hasta Pronto-----")
        break
