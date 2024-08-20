# Tema 6: clases en Python

# Subtema 6.1 Polimorfismo:

# La palabra "polimorfismo" significa "muchas formas" y en programación se refiere a métodos/funciones/operadores con el mismo nombre 
# que pueden ejecutarse en muchos objetos o clases. Es uno de los principios fundamentales de la programación orientada a objetos.

# Un ejemplo común en Python es la función len() que puede ser utilizada en diferentes objetos.
my_str = "Hello World!"
my_list = [1, 2, 3, 4, 5]
print("\nPOLIMORFISMO EN PYTHON\n")
print("Se refiere a métodos/funciones/operadores con el mismo nombre que pueden ejecutarse en distintos tipos de datos.")
print(f"El método len() puede ser utilizado para obtener la longitud del string '{my_str}', cuyo resultado es: {len(my_str)}")
print(f"Así como también el método len() puede ser utilizado para obtener la cantidad de elementos de la lista {my_list}, cuyo resultado es: {len(my_list)}")
print('')

# Polimorfismo en clases
# El polimorfismo se utiliza a menudo en los métodos de clase, donde es posible tener varias clases con el mismo nombre de método.
# Por ejemplo, si se tienen tres clases: Car, Boat y Plane, todas pueden tener un método llamado move():
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")       # Crea un objeto de la clase Car
boat1 = Boat("Ibiza", "Touring 20")  # Crea un objeto de la clase Boat
plane1 = Plane("Boeing", "747")      # Crea un objeto de la clase Plane

print("\nPOLIMORFISMO EN CLASES Y OBJETOS\n")
print("La forma más común de polimorfismo es en los métodos de clase, donde es posible tener varias clases con el mismo nombre de método.")
print("Ejemplo de polimorfismo en clases:")
for x in (car1, boat1, plane1):
    print(f"Llamando al método move() del objeto de la clase {type(x).__name__}: ")
    x.move()
print('')

# Polimorfismo de clase de herencia
# Es posible usar polimorfismo en las clases secundarias (clases hijas).
# Ejemplo: En una clase principal llamada Vehículo de la cual heredarán las clases hijas Car, Boat y Plane. 
# Las clases secundarias heredan los métodos de Vehículo, pero pueden anularlos:
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")  # Crea un objeto de la clase Car
boat1 = Boat("Ibiza", "Touring 20")  # Crea un objeto de la clase Boat
plane1 = Plane("Boeing", "747")  # Crea un objeto de la clase Plane

print("\nPOLIMORFISMO EN CLASES DE HERENCIA\n")
print("Las clases secundarias heredan los métodos de su clase padre, pero estos métodos pueden ser sobrescritos usando el polimorfismo.")
print("Ejemplo de polimorfismo en clases de herencia:")
for x in (car1, boat1, plane1):
    print(f"Llamando a los atributos de la clase {type(x).__name__} --> Marca: {x.brand}, Modelo: {x.model}")
    print(f"Llamando al método move() del objeto de la clase {type(x).__name__}: ")
    x.move()
print('')
# Las clases secundarias heredan las propiedades y los métodos de la clase principal.
# En el ejemplo anterior, se puede ver que la clase Car está vacía, pero hereda la marca, el modelo y move() de Vehicle.
# Las clases Boat y Plane también heredan la marca, el modelo y move() de Vehicle, pero ambas anulan el método move().
# Debido al polimorfismo, es posible ejecutar el mismo método para todas las clases.


# Ejemplo de polimorfismo en un sistema de procesamiento de pagos
# En este ejemplo, se tiene un sistema de pagos que acepta diferentes métodos de pago, como tarjetas de crédito, PayPal y criptomonedas.
# Cada método de pago tiene su propia clase que implementa un método común llamado process_payment().

class PaymentMethod:
    def process_payment(self, amount):
        pass

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"Procesando el pago de {amount} con tarjeta de crédito.")

class PayPal(PaymentMethod):
    def process_payment(self, amount):
        print(f"Procesando el pago de {amount} con PayPal.")

class Crypto(PaymentMethod):
    def process_payment(self, amount):
        print(f"Procesando el pago de {amount} con criptomonedas.")

# Ejemplo de polimorfismo en un sistema de pagos
def process_transaction(payment_method, amount):
    payment_method.process_payment(amount)

# Crear diferentes métodos de pago
credit_card = CreditCard()
paypal = PayPal()
crypto = Crypto()

print("\nPOLIMORFISMO EN UN SISTEMA DE PROCESAMIENTO DE PAGOS\n")
print("Ejemplo de polimorfismo en un sistema de pagos:")
for method in (credit_card, paypal, crypto):
    print(f"Procesando una transacción usando {type(method).__name__}:")
    process_transaction(method, 100.0)
print('')
