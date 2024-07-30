import math
#https://interactivechaos.com/es/manual/tutorial-de-python/la-libreria-math

#1.calcular la distancia recorrida (m) 
# por un móvil que tiene velocidad constante 100 (m/s) durante un tiempo T 30 (Sg), 
# considerar que es un MRU (Movimiento Rectilíneo Uniforme)

import os 
if os.name=="nt": #para windows
  os.system("cls")
else: #para linux
    os.system("clear")


print("Ingrese la velocidad recorrida  ")
v = int(input())
print("Ingrese el tiempo en segundos ")
s = int(input())
dis = v * s
print("la distancia:", dis, "m")


#2.Se necesita obtener el promedio simple de un 
# estudiante a partir de sus tres notas parciales.
print("Ingrese las tres notas")
not1 = float(input())
not2 = float(input())
not3 = float(input())

total= (not1+not2+not3)/3
print("El promedio es: ", total)
     
#3.Elaborar un algoritmo que solicite el número de respuestas correctas, 
# incorrectas y en blanco, correspondientes a postulantes, y muestre su puntaje      
#final considerando, que por cada respuesta correcta tendrá 4 puntos, 
# respuestas incorrectas tendrá -1 y respuestas en blanco tendrá 0.


print("Ingrese el número de respuestas correctas:")
correctas = int(input())
print("Ingrese el número de respuestas incorrectas:")
incorrectas = int(input())
print("Ingrese el número de respuestas en blanco:")
en_blanco = int(input())

puntaje = (correctas * 4) + (incorrectas * -1) + (en_blanco * 0)
print("El puntaje final es:", puntaje)


#4.Elaborar un algoritmo que permita ingresar el 
# número de partidos ganados, perdidos y empatados, 
# por algún equipo en el torneo apertura, se debe de mostrar su puntaje total, 
# teniendo en cuenta que por cada partido ganador obtendrá 3 puntos, 
# empatado 1 punto y perdido 0 puntos.

print("Ingrese el numero de partidos ganados")
pg= int(input())
print("Ingrese el numero de partidos empatados")
pe = int(input())
print("Ingrese el numero de partidos perdidos")
pp = int(input())

ppg = pg * 3
ppe = pe * 1
pt = ppg + ppe
print("El puntaje total es: ", pt)



#5.Se requiere el algoritmo para elaborar la planilla de un empleado. 
# Para ello se disponSe requiere el algoritmo para elaborar la planilla de un empleado. Para ello se dispone de sus horas laboradas en el mes, así como de la tarifa por hora.e de sus horas laboradas en el mes, 
# así como de la tarifa por hora.

print("Ingrese sus horas laboradas en el mes:")
hlm = int(input())
print("Ingrese la tarifa por hora")
th = float(input())
p = hlm * th
print("el total de la planilla es: ", p)


#6.Elabore un algoritmo que lea los 3 lados de un triángulo cualquiera y 
# calcule su área, considerar: Si A, B y C son los lados, y S el semi perímetro.

print("Ingrese el lado A")
la = int(input())
print("Ingrese el lado B")
lb = int(input())
print("Ingrese el lado C")
lc = int(input())

ls = (la+lb+lc)/2
at = (ls * (ls - la) * (ls - lb) * (ls - lc)) ** 0.5
print("EL area del triangulo es: ", at)


#7.Elaborar un algoritmo que permita calcular el número de CDs necesarios 
# para hacer una copia de seguridad, de la información almacenada en un disco cuya capacidad se conoce. 
# Hay que considerar que el disco duro está lleno de información, además expresado en gigabyte. 
# Un CD virgen tiene 700 Megabytes de capacidad y una Gigabyte es igual a 1,024 megabyte.

print("Ingrese la capacidad del disco duro en gigabytes:")
capacidad_disco = int(input())

capacidad_cd = 700  
megabytes_por_gigabyte = 1024

capacidad_disco_megabytes = capacidad_disco * megabytes_por_gigabyte

num_cds = capacidad_disco_megabytes // capacidad_cd

print("El número de CDs necesarios es:", num_cds)


#8.Se tiene los puntos A y B en el cuadrante positivo del plano cartesiano,
# elabore el algoritmo que permite obtener la distancia entre A y B.


print("Ingrese las coordenadas del punto A:")
x1 = float(input("Ingrese la coordenada x: "))
y1 = float(input("Ingrese la coordenada y: "))

print("Ingrese las coordenadas del punto B:")
x2 = float(input("Ingrese la coordenada x: "))
y2 = float(input("Ingrese la coordenada y: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La distancia entre A y B es:", distancia)



#9.Elabora un algoritmo que permita averiguar si #una persona debe sacar su CUIL, sabiendo su año #de nacimiento. El Código Único de Identificación #Laboral (CUIL) es el número que se otorga a todo #trabajador al inicio de su actividad laboral en #relación de dependencia (mayores de 17 años) que #pertenezca al Sistema Integrado de Jubilaciones y #Pensiones (SIJP), y a toda otra persona que #gestione alguna prestación o servicio de la #Seguridad Social en la República Argentina.

def verificar_cuil(año_nacimiento, año_actual):
    edad = año_actual - año_nacimiento
    if edad > 17:
        return "Debe solicitar su CUIL."
    else:
        return "No debe solicitar su CUIL aún."

año_nacimiento = int(input("Ingrese su año de nacimiento: "))
año_actual = int(input("Ingrese el año actual: "))

resultado = verificar_cuil(año_nacimiento, año_actual)
print(resultado)


#10.Elabora un algoritmo que solicite la edad de #2 hermanos y muestre un mensaje indicando la edad #del mayor y cuantos años de diferencia tiene con #el menor.

def diferencia_edades(edad_hermano1, edad_hermano2):
    if edad_hermano1 > edad_hermano2:
        print("El Primer Hermano es el Mayor por", edad_hermano1 - edad_hermano2, "años.")
    else:
        print("El Segundo Hermano es el Mayor por", edad_hermano2 - edad_hermano1, "años.")

edad_hermano1 = int(input("Ingrese la edad del Primer Hermano: "))
edad_hermano2 = int(input("Ingrese la edad del Segundo Hermano: "))

diferencia_edades(edad_hermano1, edad_hermano2)


#11.	Se tiene registrado la producción (unidades) #logradas por un operario a lo largo de la semana #(lunes a sábado). Elabore un algoritmo que nos #muestre o nos diga si el operario recibirá #incentivos sabiendo que el promedio de producción #mínima es de 100 unidades.


def verificar_incentivos(produccion_semanal):
    promedio_produccion = sum(produccion_semanal) / len(produccion_semanal) #para obtener la longitud de un objeto, se usa para contar el número de elementos de una lista
    if promedio_produccion >= 100:
        return "El operario recibirá incentivos."
    else:
        return "El operario no recibirá incentivos."

produccion_semanal = []

print("Ingrese la producción diaria del operario de lunes a sábado:")
for i in range(6):
    produccion_diaria = int(input("Ingrese la producción del día {}: ".format(i+1)))
    produccion_semanal.append(produccion_diaria)

resultado = verificar_incentivos(produccion_semanal)
print(resultado)

#----- otra forma -------

def calcular_incentivos(produccion_semana):
    produccion_total = sum(produccion_semana)
    produccion_promedio = produccion_total / len(produccion_semana)
    if produccion_promedio >= 100:
        return "Recibirá Incentivos"
    else:
        return "No Recibirá Incentivos"

produccion_lunes = int(input("Producción del día Lunes: "))
produccion_martes = int(input("Producción del día Martes: "))
produccion_miercoles = int(input("Producción del día Miércoles: "))
produccion_jueves = int(input("Producción del día Jueves: "))
produccion_viernes = int(input("Producción del día Viernes: "))
produccion_sabado = int(input("Producción del día Sábado: "))

produccion_semana = [produccion_lunes, produccion_martes, produccion_miercoles, produccion_jueves, produccion_viernes, produccion_sabado]

mensaje_incentivos = calcular_incentivos(produccion_semana)
print(mensaje_incentivos)


#12.	Elabora un algoritmo para leer 3 números #enteros diferentes entre sí, y determinar el #número mayor de los tres.



def encontrar_mayor(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3:
        return n2
    else:
        return n3

n1 = int(input("Ingrese el primer número entero: "))
n2 = int(input("Ingrese el segundo número entero: "))
n3 = int(input("Ingrese el tercer número entero: "))

numero_mayor = encontrar_mayor(n1, n2, n3)
print("El número mayor es:", numero_mayor)


#13.	Elabora un algoritmo que sirva para #identificar el tipo de triangulo conociendo sus #tres lados.

def tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"

lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))

tipo = tipo_triangulo(lado1, lado2, lado3)
print("El triángulo es de tipo:", tipo)


#14.	Elabore un algoritmo que permita ingresar un #número entero (1 a 10), y muestre su equivalente #en romano.

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
        10: "X"
    }
    return romanos.get(numero_entero, "Número fuera de rango")

numero_entero = int(input("Ingrese un número entero entre 1 y 10: "))

equivalente_romano = convertir_a_romano(numero_entero)
print("El equivalente en romano es:", equivalente_romano)

#15.	Elabore un algoritmo que permita ingresar el #monto de venta alcanzado por un vendedor durante #el mes, luego de calcular la bonificación que le #corresponde sabiendo:


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


#------ otra forma con diccionario-------

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


#16.	Elabore un algoritmo que solicite un número #entero y muestre un mensaje indicando la vocal #correspondiente, considerando que la vocal A = 1.

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

#---otra vez con diccionario------


def obtener_vocal(numero):
    vocales = {
        1: "A",
        2: "E",
        3: "I",
        4: "O",
        5: "U"
    }
    return vocales.get(numero, "Número fuera de rango")

numero_entero = int(input("Ingrese un número entero del 1 al 5: "))

vocal_correspondiente = obtener_vocal(numero_entero)
print("La vocal correspondiente es:", vocal_correspondiente)


#17.	Se desea leer un número entero de 2 cifras y 
# #que se muestre el número de unidades, decenas que #lo componen.


def obtener_unidades_y_decenas(numero):
    unidades = numero % 10
    decenas = numero // 10
    return unidades, decenas

def es_par(numero):
    if numero != 0 and numero % 2 == 0:
        return True
    else:
        return False

numero_entero = int(input("Ingrese un número entero diferente de cero: "))

if es_par(numero_entero):
    print("El número", numero_entero, "es par.")
else:
    print("El número", numero_entero, "no es par o es cero.")

#19.	Elabore un algoritmo que contenga los número #pares del 1 al 10

print("Números pares del 1 al 10:")
numero = 2
print(numero)

for k in range(1, 5):
    numero += 2
    print(numero)

#20.	Elaborar un algoritmo que permita mostrar el #sueldo promedio de un grupo de empleados.

numero_empleados = int(input("Ingrese el número de empleados: "))
suma_sueldos = 0

if es_par(numero_entero):
    print("El número", numero_entero, "es par.")
for k in range(1, numero_empleados + 1):
    sueldo_empleado = float(input(f"Ingrese el sueldo del empleado {k}: "))
    suma_sueldos += sueldo_empleado

sueldo_promedio = suma_sueldos / numero_empleados
print("El sueldo promedio del grupo de empleados es:", sueldo_promedio)

#21.	Elaborar un algoritmo que solicite la edad de #200 personas, y que muestre cuantos son mayores y #menores de edad hay


mayores = 0
menores = 0

for k in range(1, 201):
    edad_persona = int(input(f"Ingrese la edad de la persona {k}: "))
    if edad_persona < 18:
        menores += 1
    else:
        mayores += 1

print("Cantidad de personas mayores de edad:", mayores)
print("Cantidad de personas menores de edad:", menores)

#22.	Elaborar un algoritmo que solicite 2 número #enteros y muestre su producto por el método de #sumas sucesivas.

primer_numero = int(input("Ingrese el primer número entero: "))
segundo_numero = int(input("Ingrese el segundo número entero: "))

producto = 0

for k in range(1, segundo_numero + 1):
    producto += primer_numero

print("El producto de", primer_numero, "y", segundo_numero, "es:", producto)


#23.	Elaborar un algoritmo que muestre 10 números #enteros a partir de 1 excepto los pares.

for k in range(1, 11):
    if k % 2 != 0:
        print(k)


#24.	Elabore un algoritmo que muestre los términos de la serie que sean menores a 1000.