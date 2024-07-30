#Ejercicio 1.-Crear un array unidimensional de 20 elementos con nombres de personas. 
# Visualizar los elementos de la lista debiendo ir cada uno en una fila distinta. 

def lista():
    print("escriba los nombres: ")
    nombres = []
    for i in range(3):
        nombre = input(f"digite nombre {i+1}: ")
        nombres.append(nombre)
    return nombres
    
def imprimirLista(newList):
        print(newList)
        
if __name__ == '__main__':
    newList = lista()
    imprimirLista(newList)
    
    
    
    