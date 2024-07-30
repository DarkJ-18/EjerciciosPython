#Ejercicio 2.-Hacer un programa que lea las calificaciones de un alumno en 10 asignaturas,
# las almacene en un vector y calcule e imprima su media. 

def tomarNotas():
    print("Digite las 10 notas del alumno")
    notas = []
    for i in range(3):
        nota = float(input(f"digite la nota de la materia {i+1}: "))
        notas.append(nota)
    return notas

def calcularImprimir(lista):
    promedio = sum(lista)/len(lista)
    print("El Promedio es %.2f" % promedio)
    
if __name__ == '__main__':
    
    auxNotas = tomarNotas()
    calcularImprimir(auxNotas)
    
