"""
escribir un programa donde el suuario escriba un texto y este lo invierta

ejepmlo

hola-->aloh
"""
cadena = input ("escriba el texto que desee invertir: ")
longitud = len(cadena)
cadena_invertida = ""

print(longitud)

for indice in range(longitud -1, -1, -1):
    cadena_invertida += cadena[indice]

print(cadena_invertida)

