# ¿Qué es un número aleatorio?
# Un número aleatorio NO significa que sea un número diferente cada vez. Aleatorio significa algo que no se puede predecir de manera lógica.

"""
Números pseudoaleatorios y números verdaderamente aleatorios.

- Las computadoras generan números a través de programas, que son instrucciones deterministas. Por lo tanto, los números generados son pseudoaleatorios.
- Los números pseudoaleatorios son suficientes para la mayoría de las aplicaciones (simulaciones, juegos, etc.).
- Sin embargo, para aplicaciones relacionadas con la seguridad (por ejemplo, criptografía), se necesitan números verdaderamente aleatorios, obtenidos de fuentes externas (movimientos del mouse, datos en la red, etc.).

Este script aborda la generación de números pseudoaleatorios con NumPy.
"""

# Generar números aleatorios con NumPy
# NumPy ofrece el módulo `random` para trabajar con números pseudoaleatorios.

from numpy import random
import numpy as np

print("Números aleatorios en NumPy")
print("Un número aleatorio significa que no se puede predecir de manera lógica.")

# Ejemplo 1: Generando un número aleatorio entero
print("\nEjemplo 1: Generando un número aleatorio entre 0 y 100:")
x = random.randint(100)
print(f"Resultado: {x}")
print('')

# Ejemplo 2: Generando un número aleatorio flotante
print("Ejemplo 2: Generando un número aleatorio flotante entre 0 y 1:")
x = random.rand()
print(f"Resultado: {x}")
print('')

# Generar arreglos con valores aleatorios
# NumPy permite generar arreglos con valores pseudoaleatorios, lo cual es útil para simulaciones y pruebas.
print("NumPy permite generar arreglos con valores aleatorios.")

# Ejemplo 3: Arreglo unidimensional de enteros
print("Ejemplo 3: Generando un arreglo unidimensional de tamaño 5 con enteros aleatorios entre 0 y 100:")
x = random.randint(100, size=5)
print(f"Resultado: {x}")
print('')

# Ejemplo 4: Arreglo bidimensional de enteros
print("Ejemplo 4: Generando un arreglo bidimensional de tamaño 3x5 con enteros aleatorios entre 0 y 100:")
x = random.randint(100, size=(3, 5))
print(f"Resultado: \n{x}\n")

# Ejemplo 5: Arreglo unidimensional de flotantes
print("Ejemplo 5: Generando un arreglo unidimensional de tamaño 5 con flotantes aleatorios entre 0 y 1:")
x = random.rand(5)
print(f"Resultado: {x}")
print('')

# Ejemplo 6: Arreglo bidimensional de flotantes
print("Ejemplo 6: Generando un arreglo bidimensional de tamaño 3x5 con flotantes aleatorios entre 0 y 1:")
x = random.rand(3, 5)
print(f"Resultado: \n{x}\n")

# Generar valores aleatorios a partir de un arreglo
print("El método choice() genera un valor aleatorio basado en un arreglo de valores específicos.")

# Ejemplo 7: Generar un valor aleatorio a partir de un arreglo
arr = np.array([3, 5, 7, 9])
print("Ejemplo 7: Generando un valor aleatorio a partir del arreglo:")
print(arr)
x = random.choice(arr)
print(f"Resultado: {x}")
print('')

# Ejemplo 8: Generar un arreglo de valores aleatorios a partir de un arreglo existente
print("Ejemplo 8: Generando un arreglo unidimensional de tamaño 2 a partir del arreglo original:")
print(arr)
x = random.choice(arr, size=2)
print(f"Resultado: {x}")
print('')

# Ejemplo 9: Generar un arreglo bidimensional de valores aleatorios
print("Ejemplo 9: Generando un arreglo bidimensional de tamaño 2x3 a partir del arreglo original:")
x = random.choice(arr, size=(2, 3))
print(f"Resultado: \n{x}\n")

# En NumPy es posible generar números aleatorios en función de probabilidades definidas mediante el método choice() del módulo random.
# El método choice() permite especificar la probabilidad de cada valor.
# La probabilidad se establece mediante un número entre 0 y 1, donde 0 significa que el valor nunca se producirá y 1 significa que el valor siempre se producirá.

print("Números aleatorios a partir de distribuciones")
print("En NumPy es posible generar números aleatorios en función de probabilidades definidas mediante el método choice() del módulo random. Este método permite especificar la probabilidad de cada valor individual en el arreglo.")

# Ejemplo 1: Generando un arreglo 1D con probabilidades definidas
# Generando un arreglo unidimensional de 100 valores, donde cada valor debe ser 3, 5, 7 o 9.
# Las probabilidades son:
# - 3: 0.1
# - 5: 0.3
# - 7: 0.6
# - 9: 0.0 (nunca aparecerá)
print("Ejemplo 1: Generando un arreglo que contiene 100 valores, donde cada valor debe ser 3, 5, 7 o 9, con un cierto nivel de probabilidad.")

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(f"Resultado: {x}")
print(f"Longitud del resultado: {len(x)}")
print('')
# Notas:
#   - En este ejemplo, la suma de todas las probabilidades debe ser 1.
#   - Aunque el ejemplo se ejecute múltiples veces, el valor 9 nunca aparecerá debido a su probabilidad de 0.

# Ejemplo 2: Generando un arreglo 2D con probabilidades definidas
# Generando un arreglo de 2D con 3 filas y 5 columnas (15 valores en total), donde cada valor debe ser 3, 5, 7 o 9.
# Las probabilidades son las mismas que en el ejemplo anterior.
print("Ejemplo 2: Generando un arreglo de tamaño 3x5, donde cada valor debe ser 3, 5, 7 o 9, con un cierto nivel de probabilidad.")

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(f"Resultado: \n{x}\n")

