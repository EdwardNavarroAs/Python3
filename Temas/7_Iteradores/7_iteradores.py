# Tema 5: Iteradores en Python

# Un iterador es un objeto que permite recorrer una secuencia de valores, uno a la vez.
# Los iteradores son útiles para manejar grandes cantidades de datos, 
# ya que no es necesario cargar todos los elementos en memoria simultáneamente.

# En Python, un iterador es un objeto que implementa el protocolo de iterador, 
# que consiste en los métodos __iter__() y __next__().

# ----------------------------------------------------------------------------------------------------------------------------------------
# Objetos Iterables
# Las listas, tuplas, diccionarios y conjuntos son ejemplos de objetos iterables.
# Son contenedores que pueden devolver un iterador usando el método iter().
print("\nOBJETOS ITERABLES EN PYTHON\n")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print("Las listas, tuplas, diccionarios y conjuntos son objetos iterables de los que se puede obtener un iterador")
print(f"Ejemplo de objeto iterable -> objeto: {mytuple}, tipo: {type(mytuple)}")
print(f"Iterador del objeto {type(mytuple)}: iterador: {myit}, tipo: {type(myit)} ")
print('')

# Incluso las cadenas de texto son objetos iterables y pueden devolver un iterador
my_string = "hola desde python"
print("Las cadenas de texto también son objetos iterables")
print(f"Iterador de la cadena de texto '{my_string}': iterador {my_string}, tipo: {type(my_string)}")
print('')

# También es posible hacer que otros objetos personalizados sean iterables implementando el método __iter__().
print("\nCONVIRTIENDO UN OBJETO PERSONALIZADO EN ITERABLE\n")

class CustomIterable:
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        return iter(self.data)

my_custom_iterable = CustomIterable([10, 20, 30])

for item in my_custom_iterable:
    print(f'Elemento del objeto iterable personalizado: {item}')
print('')

# En Python es posible utilizar un bucle for para iterar sobre un objeto iterable:
# Nota:
#   El bucle for en realidad crea un objeto iterador y ejecuta el método next() para cada iteración.
print("\nITERANDO SOBRE OBJETOS ITERABLES\n")
mytuple = ("apple", "banana", "cherry")

for i, element in enumerate(mytuple):
    print(f'Elemento {i+1} del objeto iterable {mytuple}')
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# Creación de un Iterador Personalizado en Python
# Para crear una clase que actúe como un iterador, se deben implementar los métodos __iter__() y __next__().
# El método __iter__() inicializa el iterador y siempre debe devolver el propio objeto iterador.
# El método __next__() es responsable de devolver el siguiente elemento en la secuencia.
# Si se llega al final de la secuencia, se debería lanzar una excepción StopIteration para detener la iteración.
print("\nITERADOR EN PYTHON\n")
print("Para crear una clase que actúe como un iterador, se deben implementar los métodos __iter__() y __next__().")
print('')

class MyNumbers:
    def __iter__(self):
        self.a = 1  # Se inicializa la variable a cuando se crea el iterador
        return self

    def __next__(self):
        x = self.a  # Guarda el valor actual de a
        self.a += 1  # Incrementa a para la próxima iteración
        return x  # Devuelve el valor actual

myclass = MyNumbers()
myiter = iter(myclass)

print("Creación de un iterador en Python")
# En este ejemplo, el iterador continúa indefinidamente. En una implementación práctica, se debe agregar una condición 
# para lanzar StopIteration cuando se alcance un valor máximo.
print(f"Ejemplo de iterador en Python: iterador: {myiter}, tipo: {type(myiter)}")
print(f"Primer elemento del iterador: {next(myiter)}")      # Salida: 1
print(f"Segundo elemento del iterador: {next(myiter)}")     # Salida: 2
print(f"Tercer elemento del iterador: {next(myiter)}")      # Salida: 3
print(f"Cuarto elemento del iterador: {next(myiter)}")      # Salida: 4
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# StopIteration
# El ejemplo anterior continuaría indefinidamente si se usaran suficientes instrucciones next() 
# o si se usara en un bucle for.
# Para evitar que la iteración continúe indefinidamente, se debe utilizar la excepción StopIteration.
# En el método __next__(), se puede agregar una condición de terminación para lanzar esta excepción 
# si la iteración se realiza una cantidad específica de veces.

print("\nStopIteration\n")
print("Un iterador puede continuar indefinidamente si se tienen suficientes instrucciones next() o si se usa en un bucle for.")
print("Para evitar esto, se debe utilizar la excepción StopIteration.\n")

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 6:  # Condición para detener la iteración después de 6 pasos
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration  # Se lanza StopIteration cuando se alcanza el límite

myclass = MyNumbers()
myiter = iter(myclass)

print("Ejemplo de StopIteration")
print("En el siguiente ejemplo, se itera sobre el objeto hasta un máximo de 6 veces:")
for i, element in enumerate(myiter):
    print(f'Elemento {i + 1}: {element}')
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# Uso de next() con un valor predeterminado
# La función next() también acepta un valor predeterminado que se devuelve si el iterador se agota.

print("\nUSO DE NEXT() CON UN VALOR PREDETERMINADO\n")
myiter = iter([1, 2, 3])

print(next(myiter, 'No more elements'))  # Salida: 1
print(next(myiter, 'No more elements'))  # Salida: 2
print(next(myiter, 'No more elements'))  # Salida: 3
print(next(myiter, 'No more elements'))  # Salida: 'No more elements'
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# Iteradores Inversos con reversed()
# Python permite iterar sobre secuencias en orden inverso usando la función reversed().

print("\nITERADORES INVERSOS CON REVERSED()\n")
my_list = [1, 2, 3, 4]
print("Iterando sobre una lista en orden inverso usando reversed():")
for item in reversed(my_list):
    print(f'Elemento: {item}')
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# Generadores y la relación con los Iteradores
# Los generadores son una forma sencilla de crear iteradores. Se definen como funciones normales pero utilizan yield en lugar de return.
# Cada vez que se llama a next() en un generador, la función se ejecuta hasta la siguiente declaración yield.
# Los generadores son útiles para crear iteradores de manera rápida y eficiente.

print("\nGENERADORES Y LA RELACIÓN CON LOS ITERADORES\n")
print("Los generadores son una forma sencilla de crear iteradores utilizando la palabra clave yield.\n")

def generador_simple():
    yield 1
    yield 2
    yield 3

gen = generador_simple()

print(f"Primer valor del generador: {next(gen)}")  # Salida: 1
print(f"Segundo valor del generador: {next(gen)}")  # Salida: 2
print(f"Tercer valor del generador: {next(gen)}")  # Salida: 3
print('')

# Cada vez que la función del generador llama a yield, devuelve un valor y pausa su ejecución, retomando desde ese punto al siguiente next().
# Ejemplo de un generador con procesamiento entre yields
def generador_con_proceso():
    print("Inicio del generador")
    yield 1  # Pausa aquí en la primera llamada a next()
    print("Después del primer yield")
    yield 2  # Pausa aquí en la segunda llamada a next()
    print("Después del segundo yield")
    yield 3  # Pausa aquí en la tercera llamada a next()
    print("Final del generador")

gen = generador_con_proceso()

print("Ejemplo de generador en Python con procesamiento entre yields:")
print(f"Primer valor del generador: {next(gen)}")  # Salida: "Inicio del generador" y "1"
print(f"Segundo valor del generador: {next(gen)}")  # Salida: "Después del primer yield" y "2"
print(f"Tercer valor del generador: {next(gen)}")  # Salida: "Después del segundo yield" y "3"
print('')
