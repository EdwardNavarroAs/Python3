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




# Ejemplo adicional: Distribuciones estadísticas
print("NumPy random también permite generar valores de distribuciones estadísticas.")

# Ejemplo 10: Generar valores siguiendo una distribución normal
print("Ejemplo 10: Generando valores siguiendo una distribución normal (media=0, desviación estándar=1):")
x = random.normal(size=10)
print(f"Resultado: {x}")
print('')

# Ejemplo 11: Generar valores de una distribución binomial
print("Ejemplo 11: Generando valores siguiendo una distribución binomial (n=10, p=0.5):")
x = random.binomial(n=10, p=0.5, size=10)
print(f"Resultado: {x}")
print('')
