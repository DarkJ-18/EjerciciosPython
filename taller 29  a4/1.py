def enteroRomano(num):
    
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

    if num in romanos:
        return romanos[num]
    else:
        return "Numero no valido"
    
if __name__ == "__main__":
    num = int(input("Ingrese un numero entero: "))
    print(enteroRomano(num))