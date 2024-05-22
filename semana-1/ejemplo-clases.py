#el nombre de la clase siempre debe empezar en mayuscula

class Persona:
    """
        existe una funcion que ejecuta cuadno isntanciamos  a nuestra clase,
        a esa funcion se le dice constructior, podemos tener mas de 1 y la forma en
        la que se utiliza en python es con el nombre __init__
    """

    """
    cuadno estamos dentro de una clase el primer parametro  de toodas las funciones
    sera self, luego de self podemos colocar  los parametros que queramos
    """

    def __init__(self, nombre, apellido, edad, altura, direccion, peso):
            """vamos a agregar propiedades a self para hacer estos es de la siguiente manera
            
            sef.nombre_de_la_propiedad = valor
            """
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            self.altura = altura
            self.direccion = direccion
            self.peso = peso
    
    def saludar(self):
        return f"Hola me llamo {self.nombre} {self.apellido}, tengo {self.edad} años de edad."
    def personaDireccion(self):
        return f"Direccon actual es: {self.direccion}"
"""
para guardar INSTANCIAR una clase, debemos simplemente llamarla por su nombre y guardarla en una variable

"""

persona1 = Persona("Pepe","Perez", 29, 1.94, "Av. el sol 333", 85.4)
print (persona1.saludar())

print (persona1.personaDireccion())
