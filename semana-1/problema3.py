"""
escribe un programa que calcule el area de un circulo 
(Area = pi * radio'2).
pide radio al usuario
"""

import math
try:
    radio = float(input("Ingrese el radio: "))
    area = math.pi * radio**2

    print (f"El area del circulo es: {area} ")
except Exception as e:
    print (f"Error: {e}")
