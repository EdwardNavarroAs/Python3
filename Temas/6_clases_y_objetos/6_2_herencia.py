from abc import ABC, abstractmethod

# Herencia
# La herencia permite definir una clase que hereda todos los métodos y propiedades de otra clase. 
# La clase padre es la clase de la que se hereda, también llamada clase base. 
# La clase hija es la clase que hereda de otra clase, también llamada clase derivada.

# Clase padre:
# Cualquier clase puede ser una clase padre, por lo que la sintaxis es la misma que la de crear cualquier otra clase:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f"Hola {self.firstname} {self.lastname}")

print("\nDEFINICIÓN DE HERENCIA EN PYTHON\n")
print("La clase padre es la clase de la que se hereda. Cualquier clase en Python puede ser una clase padre y no tiene ningún tipo de sintaxis especial.")
x = Person("John", "Doe")
print(f"Llamando al método 'printname' de la clase padre {type(x)}:")
x.printname()
print('')

# Clase hija:
# Para crear una clase que herede la funcionalidad de otra clase, se debe enviar la clase principal o padre como 
# parámetro al crear la clase secundaria o hija.
# Nota:
#   - La clase hija tiene las mismas propiedades y métodos que la clase Padre.
class Student(Person):
    pass

print("La clase hija es la clase que hereda de otra clase. Para crear una clase hija se debe agregar como parámetro la clase padre.")
y = Student("Mike", "Olsen")
print(f"Llamando al método 'printname' de la clase padre {type(x)} a través de la clase hija {type(y)}:")
y.printname()
print('')

# La clase hija puede tener sus propios parámetros y métodos.
# Cuando se agrega la función __init__() en la clase hija, esta ya no heredará la función __init__() de la clase padre. Por lo tanto, 
# la función del hijo anula la herencia de la función del padre __init__()
print("\nCLASES HIJAS EN PYTHON\n")
class Student(Person):
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        # add properties, etc.

print("Ejemplo de la clase hija que anula el método __init__ de la clase padre:")
y = Student("Anna", "Smith")
print(f"Llamando al método 'printname' de la clase hija {type(y)} (no hereda el __init__ de la clase padre):")
y.printname()  # Esto causará un error porque no se ha llamado al constructor de la clase padre para inicializar los atributos firstname y lastname
print('')

# Para mantener la herencia de todos los métodos y propiedades de la clase padre, se debe utilizar la función super() en la clase hija.
# Al usar la función super(), la clase hija heredará automáticamente los métodos y propiedades de la clase padre.
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

print("Ejemplo de la clase hija utilizando super() para heredar el método __init__ de la clase padre:")
y = Student("Anna", "Smith")
print(f"Llamando al método 'printname' de la clase hija {type(y)}:")
y.printname()
print('')

# Es posible agregar propiedades a la clase hija agregando nuevos parámetros a la función __init__() de la clase hija. 
# Esto crea un parámetro que solo pertenece a la hija, además de heredar todos los parámetros de la clase padre.
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print("Ejemplo de la clase hija con una propiedad adicional (graduationyear):")
print(f"Nombre: {x.firstname} {x.lastname}, Año de graduación: {x.graduationyear}")
print('')

# Es posible agregar métodos a la clase hija, además de los métodos heredados de la clase padre.
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(f"Saludos {self.firstname} {self.lastname} desde una clase hija en Python. Año de graduación: {self.graduationyear}")

p1 = Student("Edward", "Navarro", 2024)
print("Ejemplo de la clase hija con un método adicional (welcome):")
p1.welcome()
print('')

# Herencia Múltiple
# Python permite heredar de múltiples clases. Esto se hace simplemente listando varias clases padres
#  entre paréntesis cuando se define la clase hija.
class Father:
    def __init__(self, fname):
        self.fname = fname

    def print_father(self):
        print(f"Padre: {self.fname}")

class Mother:
    def __init__(self, mname):
        self.mname = mname

    def print_mother(self):
        print(f"Madre: {self.mname}")

class Child(Father, Mother):
    def __init__(self, fname, mname, cname):
        Father.__init__(self, fname)
        Mother.__init__(self, mname)
        self.cname = cname

    def print_child(self):
        print(f"Hijo: {self.cname}")

print("\nHERENCIA MÚLTIPLE EN PYTHON\n")
child = Child("John", "Jane", "Mike")
child.print_father()
child.print_mother()
child.print_child()
print('')

# Clases Abstractas y Métodos Abstractos
# Las clases abstractas y los métodos abstractos proporcionan una forma de definir una interfaz para las clases que las heredan. 
# Una clase abstracta no puede ser instanciada directamente y está diseñada para ser una clase base de otras clases.
#   Clases abstractas: Una clase abstracta es una clase que no está destinada a ser instanciada. En su lugar, 
#                      está diseñada para ser heredada por otras clases. Las clases abstractas pueden contener métodos abstractos, 
#                      que son métodos declarados pero que no tienen una implementación.
#   Métodos abstractos: Un método abstracto es un método que se declara en una clase base pero que no tiene implementación. 
#                       Las subclases que heredan de la clase base deben proporcionar una implementación para los métodos abstractos.
# Para definir clases y métodos abstractos en Python, utilizamos el módulo abc (Abstract Base Classes).
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """
        Método abstracto que debe ser implementado por cualquier subclase.
        """
        pass

# Ejemplo de subclases que implementan el método abstracto

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Intentar instanciar una clase abstracta directamente producirá un error
# animal = Animal()  # Esto producirá un error

print("\nCLASES ABSTRACTAS Y MÉTODOS ABSTRACTOS EN PYTHON\n")
dog = Dog()
cat = Cat()
print(f"El perro hace: {dog.make_sound()}")
print(f"El gato hace: {cat.make_sound()}")
print('')

# ejemplo 2 con múltiples métodos abstractos
class Shape(ABC):
    @abstractmethod
    def area(self):
        """
        Método abstracto para calcular el área.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Método abstracto para calcular el perímetro.
        """
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

print("Ejemplo de clases derivadas que implementan múltiples métodos abstractos:")
rect = Rectangle(4, 5)
circle = Circle(3)
print(f"Área del rectángulo: {rect.area()}, Perímetro del rectángulo: {rect.perimeter()}")
print(f"Área del círculo: {circle.area()}, Perímetro del círculo: {circle.perimeter()}")
print('')