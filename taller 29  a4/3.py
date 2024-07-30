#Ejercicio 3: Crear un Diccionario de Estudiantes 
# Crea un diccionario donde las claves sean los nombres de los estudiantes 
# y los valores sean sus calificaciones.


def crearDiccionarioEstudiantes(): 

    estudiantes = { 
        "Luis": 92, 
        "Carlos": 78, 
        "María": 95, 
        "Pedro": 88,
        "Ana": 85,
        "Nicolas":75
    } 

    return estudiantes


if __name__=="__main__":

    dicNotas=crearDiccionarioEstudiantes()
    print(dicNotas)

    nom=input("nombre del nuevo estudiante: ")
    nota=int(input("nota del nuevo estudiante: "))
    dicNotas[nom]=nota

    print(dicNotas)
    promedio=sum(dicNotas.values())/len(dicNotas)
    print(f"el promedio del salon es {promedio}")
    estudiantesMayor89=[clave for clave, valor in dicNotas.items() if valor>=90]
    print(estudiantesMayor89)
    #

