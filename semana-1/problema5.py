"""
escrie una funcion mas_de_tres que reciba tres numeros
 y vuelva el mayor de ellos
"""

def max_de_tres(n1, n2, n3):
    return max(n1, n2, n3)

    #n1 = input (input("ingrese el numero 1: "))
    #n2 = input (input("ingrese el numero 2: "))
    #n3 = input (input("ingrese el numero 3: "))

    #print (max_de_tres(n1, n2, n3))
 
numeros = input ("ingrese los numeros separados por, :")

"""
split: convierte un stri a un list, basado en un  operador
ejemplo:
"10-11-12", split("-")
["10","11", "12"]

destructuracion
n1, n2, n3 = ["10","11", "12"]
"""
print(numeros.split(","))
n1, n2 ,n3 = numeros.split(",")
print(max_de_tres(int(n1), int(n2), int(3)))