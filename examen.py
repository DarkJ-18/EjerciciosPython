#USANDO ELIF y Try Except: Desarrolla un algoritmo en Python que solicite al usuario 
# ingresar tres números y luego imprima el mayor de los tres, el menor de los 3, si son iguales, 
# si al menos hay dos iguales. Asegúrate de que tu código maneje 
# correctamente cualquier tipo de números (positivos, negativos y decimales).

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    if num1 > num2 and num1 > num3:
        print("El número mayor es: ", num1)
    elif num2 > num1 and num2 > num3:
        print("El número mayor es: ", num2)
    elif num3 > num1 and num3 > num2:
        print("El número mayor es: ", num3)
    else:
        print("Los números son iguales")
    if num1 < num2 and num1 < num3:
        print("El número menor es: ", num1)
    elif num2 < num1 and num2 < num3:
        print("El número menor es: ", num2)
    elif num3 < num1 and num3 < num2:
        print("El número menor es: ", num3)
    else:
        print("Los números son iguales")
    if num1 == num2 or num1 == num3 or num2 == num3:
        print("Al menos hay dos números iguales")
except:
    print("Ingrese solo numeros")
