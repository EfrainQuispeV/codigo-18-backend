""""
escriba una funcion contar_palabras que reciba una cadena
y devuleva el numero de palabras que contiene

hola como estas
3

nota:
len cuenta las palabras
.
"""

def contar_palabras(palaras):
     return len(palaras.split(" "))

#hola como estas

palabras = input ("ingrese algunas palabras: ")
print (contar_palabras(palabras))