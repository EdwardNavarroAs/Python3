import numpy as np
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# ACCEDIENDO A ELEMENTOS DE UN ARREGLO
# # La indexación en NumPy es similar a la de las listas de Python.
# Se accede a un elemento de un arreglo mediante su número de índice.
# Los índices de los arreglos de NumPy comienzan en 0, por lo que el primer elemento tiene índice 0, el segundo índice 1, y así sucesivamente.

arr = np.array([1, 2, 3, 4])

print("Es posible acceder a un elemento de un arreglo de NumPy mediante la indexación.")
print("Ejemplo 1: Accediendo al primer elemento del arreglo:")
print(arr)
print(f"Elemento obtenido: {arr[0]}\n")

# Acceso a matrices 2D
# En una matriz 2D, se usa un par de índices (fila, columna) para acceder a un elemento.
# Las matrices 2D pueden verse como una tabla de filas y columnas, donde el primer índice representa la fila y el segundo índice la columna.
arr2D = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print("Para acceder a elementos de matrices 2D, se usan índices separados por comas que representan la fila y la columna.")
print("Ejemplo 2: Accediendo al segundo elemento de la primera fila del arreglo:")
print(arr2D)
print(f"Elemento obtenido: {arr2D[0, 1]}\n")

# Acceso a matrices 3D
# En una matriz 3D, se usan tres índices: el primero para la profundidad, el segundo para la fila, y el tercero para la columna.
arr3D = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("Ejemplo 3: Accediendo al segundo elemento del segundo arreglo dentro del primer arreglo en una matriz 3D:")
print(arr3D)
print(f"Elemento obtenido: {arr3D[0, 1, 1]}\n")

# Indexación negativa
# Para acceder a un arreglo desde el final hacia adelante, es posible utilizar la indexación negativa.
# El índice -1 representa el último elemento, -2 el penúltimo, y así sucesivamente.
print("Para acceder a elementos de un arreglo desde el final hacia adelante, se utiliza la indexación negativa.")
print("Ejemplo 4: Accediendo al penúltimo elemento de la primera fila de una matriz 2D:")
print(arr2D)
print(f"Elemento obtenido: {arr2D[0, -2]}\n")
