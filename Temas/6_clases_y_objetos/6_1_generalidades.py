# Tema 6: clases en Python

# Subtema 6.1 Generalidades:
# Python es un lenguaje de programación orientado a objetos. Casi todo en Python es un objeto, con sus propiedades y métodos.
# Una clase es como un constructor de objetos o un "modelo" para crear objetos.

# Para crear una clase, se debe utilizar la palabra clave class:
class MyClass:  # nombre de la clase
    x = "hola desde una clase en Python"  # atributo de la clase

print("\nDEFINICIÓN DE UNA CLASE EN PYTHON\n")
print("Una clase es un constructor de objetos o un modelo para crear objetos.")
print("Un objeto es una instancia de la clase que puede tener propiedades y métodos.")
# Para crear un objeto se debe utilizar la sintaxis MyClass()
# Un objeto de una clase es una instancia de la clase. Es decir, una clase actúa como un "molde" 
# para crear objetos específicos con propiedades y comportamientos definidos por la clase.
c1 = MyClass()  # instancia de la clase
print(f"Accediendo al atributo de la clase {type(MyClass())}, atributo: {c1.x}")
print('')

# Los ejemplos anteriores son clases y objetos en su forma más simple y no son realmente útiles en aplicaciones reales.
# Para comprender el significado de las clases, es necesario entender la función __init__() incorporada.

# Todas las clases tienen una función llamada __init__(), que siempre se ejecuta cuando se inicia la clase.
# La función __init__() se utiliza para asignar valores a las propiedades del objeto u otras operaciones que sean necesarias cuando se crea el objeto.
# Nota:
#   La función __init__() se llama automáticamente cada vez que se utiliza la clase para crear un nuevo objeto.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print("\nFUNCIÓN __init__() DE UNA CLASE EN PYTHON\n")
print("La función __init__() se utiliza para asignar valores a los atributos de una clase.")
p1 = Person("John", 36)
p2 = Person("Andrea", 25)
print("Se crea la clase Person y se instancian los objetos p1 y p2.")
print(f"Instancia 1 de la clase Person: nombre: {p1.name}, edad: {p1.age}")
print(f"Instancia 2 de la clase Person: nombre: {p2.name}, edad: {p2.age}")

# La función __str__() controla lo que se debe devolver cuando el objeto de clase se representa como una cadena.
# Si la función __str__() no está configurada, se devuelve la representación de cadena predeterminada del objeto:
print("\nFUNCIÓN __str__() DE UNA CLASE EN PYTHON\n")
print("La función __str__() controla lo que se debe devolver cuando el objeto de clase se representa como una cadena.")

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # Define el formato de la cadena que se retorna cuando se llama al objeto de la clase
        return f"El objeto creado es: {self.name}({self.age})"

p1 = Person1("John", 36)
print("Ejemplo de representación de cadena de un objeto SIN la función __str__():")
print(p1)
print('')

p2 = Person2("Natalia", 22)
print("Ejemplo de representación de cadena de un objeto CON la función __str__():")
print(p2)
print('')

# Métodos de instancia
# Además de los atributos, las clases pueden tener métodos, que son funciones definidas dentro de la clase que operan sobre sus instancias u objetos.
print("\nMÉTODOS DE INSTANCIA EN UNA CLASE EN PYTHON\n")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} está ladrando."

    def get_age(self):
        return f"{self.name} tiene {self.age} años."

dog1 = Dog("Fido", 4)
print("Los métodos de una clase son funciones definidas dentro de la clase que operan sobre los objetos.")
print("Ejemplo del uso de métodos de una clase en Python:")
print(dog1.bark())
print(dog1.get_age())
print('')

# Parámetro self:
# El parámetro self es una referencia a la instancia actual de la clase y se utiliza para acceder a variables que pertenecen a la clase.
# No es necesario que el parámetro se llame self, en realidad puede tener cualquier nombre, pero debe ser el primer parámetro de cualquier función de la clase.
# Sin embargo, por convención y buenas prácticas se utiliza la palabra self en la gran mayoría de aplicaciones.
print("\nPARÁMETRO SELF DE UNA CLASE EN PYTHON\n")
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hola, mi nombre es " + abc.name)

p1 = Person("John", 36)
print("El parámetro self puede tener cualquier otro nombre.")
p1.myfunc()
print('')

# En python es posible modificar las propiedades de los objetos:
print("\nMODIFICANDO LAS PROPIEDADES DE LOS OBJETOS\n")
print("En Python es posible modificar las propiedades de los objetos.")
print(f"Valor inicial del atributo age del objeto p1: {p1.age}")
p1.age = 40
print(f"Valor modificado del atributo age del objeto p1: {p1.age}")
print('')

# En Python es posible eliminar un objeto mediante la palabra clave "del"
print("\nELIMINANDO UN OBJETO EN PYTHON\n")
print("Eliminando un objeto.")
del p1
print('')

# Las definiciones de clases en Python no pueden estar vacías, 
# pero si por alguna razón se necesita definir una función sin contenido, se debe utilizar la palabra clave pass.
class Person:
    pass
