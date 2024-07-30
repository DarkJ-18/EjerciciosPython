# Elabore un algoritmo que permita ingresar un #número entero (1 a 10), y muestre su equivalente #en romano.
import os 
if os.name=="nt": #para windows
  os.system("cls")
else: #para linux
    os.system("clear")

def convertir_a_romano(numero_entero):
    romanos = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
    }
    return romanos.get(numero_entero, "Número fuera de rango")

numero_entero = int(input("Ingrese un número entero entre 1 y 10: "))

equivalente_romano = convertir_a_romano(numero_entero)
print("El equivalente en romano es:", equivalente_romano)


# 15.Elabore un algoritmo que permita ingresar el #monto de venta alcanzado por un vendedor durante #el mes, luego de calcular la bonificación que le #corresponde sabiendo:


def calcular_bonificacion(monto_venta):
    if monto_venta <= 1000:
        bonificacion = 0
    elif monto_venta <= 5000:
        bonificacion = 3
    elif monto_venta <= 20000:
        bonificacion = 5
    else:
        bonificacion = 8
    return bonificacion

monto_venta = float(input("Ingrese el monto de venta alcanzado por el vendedor durante el mes: "))

bonificacion = calcular_bonificacion(monto_venta)
print("La bonificación correspondiente es:", bonificacion)


# ------ otra forma con diccionario-------

def calcular_bonificacion(monto_venta):
    bonificaciones = {
        range(0, 1000): 0,
        range(1000, 5000): 3,
        range(5000, 20000): 5,
        range(20000, float('inf')): 8
    }
    for rango, bonificacion in bonificaciones.items():
        if monto_venta in rango:
            return (bonificacion * monto_venta) / 100

monto_venta = float(input("Ingrese el monto de venta alcanzado por el vendedor durante el mes: "))

total_bonificacion = calcular_bonificacion(monto_venta)
print("La bonificación correspondiente es:", total_bonificacion)


# 16. Elabore un algoritmo que solicite un número
# #entero y muestre un mensaje indicando la vocal
# #correspondiente, considerando que la vocal A = 1.

def obtener_vocal(numero):
    switch = {
        1: "A",
        2: "E",
        3: "I",
        4: "O",
        5: "U"
    }
    return switch.get(numero, "Valor Incorrecto")

numero_entero = int(input("Ingrese un número entero del 1 al 5: "))

vocal_correspondiente = obtener_vocal(numero_entero)
print("La vocal correspondiente es:", vocal_correspondiente)

# 17
# Ejercicio 1: Clasificación de edades.

# Escribe un programa que reciba una edad como entrada
# y clasifique a la persona en las siguientes categorías:
# niño (menos de 11 años), adolescente (12-17 años),
# adulto (18-64 años) o mayor (65 años o más).
# Opcional: preadolescente: 11 a 13 y adolescente de 14 a 17


edad = int(input("Ingrese su edad: "))
try:
    if edad <=11:
        print("Niño")
    elif 12<= edad <=17:
        print("Adolescente")
    elif 18<=edad <=64:
        print("adulto")
    elif edad >=65:
        print("Mayor")
except:
    print("Ingrese solo numeros")

# 18   Escribe un programa que reciba una nota (0-100)
# y la clasifique en: deficiente (menos de 50), aprobado (50-64),
# notable (65-84), sobresaliente (85-100).

nota = int(input("Ingrese la nota: "))
if nota < 50:
    print("Deficiente ")
elif 50 <= nota < 65:
    print("Aprobado")
elif 65 <= nota < 85:
    print("Notable")
elif 85 <= nota <= 100:
    print("Sobresaliente")
else:
    print ("Nota fuera del rango permitido.")


# 19. Ejercicio 3: Clasificación de temperaturas.
# Escribe un programa que reciba una temperatura
# (en grados Celsius) y la clasifique en: frío
# (menos de 10°C), templado (10-20°C), cálido (21-30°C)
# o caluroso (más de 30°C).


temp = float (input ("Introduce la temperatura en grados Celsius: "))
if temp < 10:
    print("Frío")
elif temp >= 10 and temp <= 20:
    print("Templado")
elif temp >= 21 and temp <= 30:
    print("Cálido")
elif temp > 30:
    print("Caluroso")


# 20. Ejercicio 4: Clasificación de IMC.
# Escribe un programa que reciba el Índice de Masa Corporal (IMC)
# de una persona y lo clasifique en: bajo peso (menos de 18.5),
# normal (18.5-24.9), sobrepeso (25-29.9) u obeso (30 o más).

imc = float(input("Ingrese su IMC: "))
if imc < 18.5:
    print ("Bajo peso")
elif 18.5 <= imc < 25:
       print("Normal")
elif 25 <= imc < 30:
       print("Sobrepeso")
elif imc >= 30:
       print("Obeso")

# 21. Ejercicio 5: Evaluación del viento.
# Escribe un programa que reciba la velocidad del viento (en km/h)
# y la clasifique en: calmado (menos de 5 km/h), ligero (5-19 km/h),
# moderado (20-39 km/h) o fuerte (más de 40 km/h).

velocidad = float (input ("Introduce la velocidad del viento en km/h: "))
if velocidad < 5:
    print("Viento calmado")
elif 5 <= velocidad < 20:
    print("Viento ligero")
elif 20 <= velocidad < 40:
    print("Viento moderado")
elif velocidad >= 40:
    print("Viento fuerte")

# 22. Ejercicio 6: Clasificación de automóviles.
# Escribe un programa que reciba la velocidad máxima
# de un automóvil (en km/h) y lo clasifique en: económico (menos de 140 km/h),
# estándar (140-180 km/h),
# deportivo (181-220 km/h) o de alto rendimiento (más de 220 km/h).

velocidad = float(input("Introduce la velocidad máxima del automóvil en km/h: "))
if velocidad < 140:
    print("Automóvil económico")
elif 140 <= velocidad <= 180:
    print("Automóvil estándar")
elif 181 <= velocidad <= 220:
    print("Automóvil deportivo")
elif velocidad > 220:
    print("Automóvil de alto rendimiento")

# 23. Ejercicio 7: Clasificación de alturas.
# Escribe un programa que reciba la altura de una persona (en centímetros)
# y la clasifique en: baja (menos de 150 cm), promedio (150-180 cm)
# o alta (más de 180 cm).
