#Ejercicio 4.- crea una tupla con la información de un participante del torneo de ajedrez y luego imprime cada 
# uno de los elementos de la tupla con una descripción adecuada:
def crearParticipante():
    participante =["Juan",23,"Colombia",70]
    return participante
def imprimirParticipante(participante):
    print(participante[0])
    print(participante[1])
    print(participante[2])
    print(participante[3])
    
if __name__ == '__main__':
    temp=crearParticipante()
    imprimirParticipante(temp)
    