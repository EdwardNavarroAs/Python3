# Permutaciones aleatorias de elementos
# Una permutación se refiere a una disposición de elementos.
# Por ejemplo, [3, 2, 1] es una permutación de [1, 2, 3], y viceversa.

from numpy import random
import numpy as np

print("Permutaciones en NumPy")
print("Una permutación se refiere a la disposición que tienen los elementos en un arreglo NumPy.")

# Ejemplo 1: Introducción a las permutaciones
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 5, 4, 1, 2])
print(f"\nEjemplo 1: El arreglo {arr1} es una permutación del arreglo {arr2}")
print('')

# El módulo Random de NumPy proporciona dos métodos para trabajar con permutaciones: shuffle() y permutation().

# Mezclando arreglos NumPy con shuffle()
# El método shuffle() cambia la disposición de los elementos en el lugar, es decir, modifica el arreglo original.
print("El módulo random de NumPy permite cambiar la disposición de los elementos de un arreglo NumPy.")
print("Ejemplo 2: Cambiando la disposición de los elementos utilizando el método shuffle() de random NumPy.")
print(f"Arreglo original: {arr1}")
random.shuffle(arr1)
print(f"Arreglo modificado (shuffle): {arr1}")
print('')

# Generando permutaciones de arreglos con permutation()
# El método permutation() genera una nueva disposición de los elementos del arreglo original,
# devolviendo un nuevo arreglo sin modificar el arreglo original.
print("Ejemplo 3: Generando una nueva disposición de los elementos utilizando el método permutation() de random NumPy.")
arr2 = np.array([3, 5, 4, 1, 2])  # Reinicializamos para demostrar el comportamiento
print(f"Arreglo original: {arr2}")
x = random.permutation(arr2)
print(f"Nuevo arreglo permutado (permutation): {x}")
print(f"Arreglo original permanece sin cambios: {arr2}")
print('')

# Ejemplo adicional 1: Aplicando shuffle() a arreglos multidimensionales
# El método shuffle() solo afecta al primer eje del arreglo, es decir, mezcla las filas en arreglos bidimensionales.
print("Ejemplo adicional 1: Usando shuffle() en un arreglo bidimensional:")
arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Arreglo original:")
print(arr2D)
random.shuffle(arr2D)
print("Arreglo después de aplicar shuffle:")
print(arr2D)
print('')

# Ejemplo adicional 2: Aplicando permutation() a arreglos multidimensionales
# A diferencia de shuffle(), permutation() devuelve una copia del arreglo con el eje especificado permutado.
print("Ejemplo adicional 2: Usando permutation() en un arreglo bidimensional:")
arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Arreglo original:")
print(arr2D)
x = random.permutation(arr2D)
print("Nuevo arreglo permutado (permutation):")
print(x)
print("El arreglo original permanece sin cambios:")
print(arr2D)
print('')

# Ejemplo adicional 3: Permutando números enteros directamente con permutation()
# Si se pasa un número entero al método permutation(), genera una permutación de los números en el rango 0 a n-1.
print("Ejemplo adicional 3: Generando una permutación de enteros del 0 al 9:")
x = random.permutation(10)
print(f"Permutación de enteros: {x}")
print('')
