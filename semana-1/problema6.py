"""
escriba una funcion la cual reciba un numero entero 
y retorne la sua de sus valores

ejemplo:

2536 => 2+5+3+3+6 = 16

nota: string si es posible hacer for
"""

def sum_digits(numero):
    suma = 0
    for n in numero:
        suma += int(n)

    return suma

numero = input("Escriba un numero: ")
print(sum_digits(numero))