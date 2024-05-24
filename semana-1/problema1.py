#escriba un programa que retorne la suma de 2 numeros
numero_1 = input ("ingresa numero 1:  ")
numero_2 = input ("ïngresa numero 2:  ")

#type (variable) permite ver el tipo de dato
print (type (numero_1), type(numero_2))

"""
nos indica que toda informacion sera un 'str' (string)
"""

#suma = int (numero_1) + int(numero_2)
"""
si queremos convertir un stri a int usamos la funsion int(variables)
si queremos convertir un str a float usamos la funcion float (variable)

el try va a intentar, en caso de haber un erro va a saltar un error
"""
try: 

    suma = float (numero_1) + float(numero_2)
    print (suma)
except Exception as e:  
    print(e)