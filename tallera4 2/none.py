#None es un tipo de dato especial en Python que representa la ausencia de un valor o la falta de definición de un objeto. 
# Es similar al concepto de null en otros lenguajes de programación.

#En Python, None es un singleton, lo que significa que solo hay una instancia de este objeto en todo el programa.
# Se utiliza comúnmente para indicar que una variable o una función no tiene un valor asignado o no devuelve nada.

#1
def funcion_sin_retorno():
    print("Esta función no devuelve nada")

# La función se ejecuta, pero no devuelve ningún valor
resultado = funcion_sin_retorno()
print(resultado)  # Esto imprimirá None

#2
def funcion_con_argumento(arg=None):
    if arg is None:
        print("No se proporcionó ningún argumento")
    else:
        print("El argumento es:", arg)

funcion_con_argumento()  # Imprimirá "No se proporcionó ningún argumento"



