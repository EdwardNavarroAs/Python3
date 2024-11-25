# Ordenar arreglos en NumPy
# Ordenar significa colocar elementos en una secuencia ordenada.
# Una secuencia ordenada es cualquier secuencia que tenga un orden correspondiente a los elementos, como numérico o alfabético, ascendente o descendente.
# El objeto ndarray de NumPy tiene una función llamada sort(), que ordenará un arreglo de forma específica.
# Nota:
#    Este método devuelve una copia del arreglo, sin modificar el arreglo original.

import numpy as np

print("Ordenando arreglos en NumPy")
print("Ordenar significa colocar elementos en un orden específico.")

# Ejemplo 1: Ordenando un arreglo unidimensional de enteros
print(f"\nEjemplo 1: Ordenando un arreglo unidimensional:")
arr = np.array([3, 2, 0, 1])
print("Arreglo original:")
print(arr)
x = np.sort(arr)
print("Arreglo ordenado:")
print(x)
print('')

# Ejemplo 2: Ordenando un arreglo unidimensional de cadenas de texto
print("Ejemplo 2: Ordenando un arreglo unidimensional de tipo cadena de texto:")
arr = np.array(['banana', 'cherry', 'apple'])
print("Arreglo original:")
print(arr)
x = np.sort(arr)
print("Arreglo ordenado:")
print(x)
print('')

# Ejemplo 3: Ordenando un arreglo unidimensional de valores booleanos
print("Ejemplo 3: Ordenando un arreglo unidimensional de tipo booleano:")
arr = np.array([True, False, True])
print("Arreglo original:")
print(arr)
x = np.sort(arr)
print("Arreglo ordenado:")
print(x)
print('')

# Ejemplo 4: Ordenando un arreglo bidimensional (por filas)
print("Ejemplo 4: Ordenando un arreglo bidimensional (por filas):")
arr = np.array([[3, 2, 4], [5, 0, 1]])
print("Arreglo original:")
print(arr)
x = np.sort(arr)  # Ordena por filas de manera predeterminada (axis=1)
print("Arreglo ordenado:")
print(x)
print('')

# Ejemplo 5: Ordenando un arreglo bidimensional a lo largo de las columnas
print("Ejemplo 5: Ordenando un arreglo bidimensional a lo largo de las columnas (axis=0):")
arr = np.array([[3, 2, 4], [5, 0, 1]])
print("Arreglo original:")
print(arr)
x = np.sort(arr, axis=0)  # Ordena por columnas
print("Arreglo ordenado:")
print(x)
print('')

# Ejemplo adicional: Ordenando un arreglo multidimensional
print("Ejemplo adicional: Ordenando un arreglo tridimensional:")
arr = np.array([[[3, 2, 1], [6, 5, 4]], [[9, 8, 7], [12, 11, 10]]])
print("Arreglo original:")
print(arr)
x = np.sort(arr)  # Ordena a lo largo del último eje por defecto (axis=-1)
print("Arreglo ordenado (a lo largo del último eje):")
print(x)
print('')
