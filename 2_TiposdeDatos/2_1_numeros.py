# Tema 2: Tipos de datos en python
# 2.1 números
import random

# Hay tres tipos numéricos en Python: int, float, complex
#Las variables de tipo numérico se crean cuando se les asignas un valor
print(f"Las variables de tipo numérico se crean cuando se les asigna un valor")
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(f"tipo de dato entero: ({x}, {type(x)}), tipo de dato flotante: ({y}, {type(y)}), tipo de dato complejo: ({z}, {type(z)})")
print('')

# los números enteros,pueden ser positivos o negativos, sin decimales y de longitud ilimitada
print("ejemplos de tipos de datos enteros:")
x1 = 35656222554887711
x2 = -3255522
print(f"x1: {x1}, x2: {x2}")
print('')

# Un número de punto flotante" es un número, positivo o negativo, que contiene uno o más decimales.
print("ejemplos de tipos de datos de punto flotante:")
y1 = 1.10
y2 = 12E4
y3 = -35.59
print(f"y1: {y1}, y2: {y2}, y3: {y3}")
print('')

# Los números complejos se escriben con una "j" como parte imaginaria
print("ejemplos de tipos de datos complejos:")
z1 = 3+5j
z2 = 5j
z3 = -5j
print(f"z1: {z1}, z2: {z2}, z3: {z3}")
print('')

# Los números binarios son numeros que utilizan únicamente dos dígitos: 0 y 1.
print("ejemplos de tipos de datos binarios:")
x = 0b0001
y = 0b0011
print(f"representacion binaria del {x} = {bin(x)}")
print(f"representacion binaria del {y} = {bin(y)}")
print('')

# conversión de tipo 
# es posible convertir de un tipo numerico a otro mediante las funciones de python
# Nota: No es posible convertir números complejos a otro tipo de número.
print("es posible convertir de un tipo a otro utilizando los metodos de python")
x = 1
y = 2.8  
z = 1j   

a = float(x)    # convert from int to float
b = int(y)      # convert from float to int
c = complex(x)  # convert from int to complex
print(f"(dato original: ({x}, {type(x)}) --> conversion: ({a}, {type(a)})),
      (dato original: ({y}, {type(y)}) --> conversion: ({b}, {type(b)})), 
      (dato original: ({z}, {type(z)}) --> conversion: ({c}, {type(c)}))")
print('')

# Python no tiene una función para crear un número aleatorio, sin embargo, si tiene un módulo integrado llamado random que se utiliza para crear números aleatorios
print("creando un número aleatorio en python")
r = random.randrange(1, 10)     # número aleatorio entre 1 y 9 (no incluye el 10)
print(f"número aleatorio: {r}")
print('')
