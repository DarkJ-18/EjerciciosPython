#En Python, exit es una función que forma parte del módulo sys y es un alias de sys.exit.
# Por lo tanto, en términos de funcionalidad, exit y sys.exit son lo mismo:
# ambos se utilizan para finalizar la ejecución de un script de Python de forma inmediata.
import sys
nombre_usuario="pepe"
usuario_autenticado=True
# Verificar si el usuario está autenticado
if usuario_autenticado:    
    print ("Bienvenido,", nombre_usuario)
else:
    # Si el usuario no está autenticado, salir del script
    sys.exit ("Error: El usuario no está autenticado")

# El resto del código aquí solo se ejecutará si el usuario está autenticado
print(nombre_usuario,", Tu Panel del usuario esta activado...")
print("preparando las demás opciones del panel del usuario...")
