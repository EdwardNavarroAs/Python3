# NumPy es una biblioteca de Python utilizada para trabajar con arreglos (arrays).
# NumPy incluye funciones para álgebra lineal, transformada de Fourier y operaciones avanzadas con arreglos.
# Fue creada en 2005 por Travis Oliphant como un proyecto de código abierto.
# Su nombre "NumPy" proviene de "Numeric Python".

"""
¿Por qué utilizar NumPy?

Las listas en Python pueden actuar como arreglos, pero su procesamiento es lento.

NumPy busca proporcionar un objeto de arreglo (array) que es hasta 50 veces más rápido que las listas tradicionales de Python.

El objeto principal de arreglo en NumPy se llama ndarray y proporciona muchas funciones de soporte que hacen que trabajar con ndarrays sea muy fácil y eficiente.

Los arreglos se utilizan de manera frecuente en la ciencia de datos, donde la velocidad y los recursos son críticos.

Nota: La Ciencia de Datos es una rama de la informática que estudia cómo almacenar, analizar y derivar información útil de los datos.
"""

"""
Diferencia entre tensores, vectores y matrices:

- **Vector**: Es un arreglo unidimensional (1-D). Representa una lista de elementos y no tiene subniveles. 
- **Matriz**: Es un arreglo bidimensional (2-D) y puede pensarse como una tabla de valores con filas y columnas.
- **Tensor**: Es una generalización de los vectores y matrices a más dimensiones. Un tensor puede tener tres o más dimensiones, permitiendo representar datos complejos.

NumPy permite manejar de manera eficiente estas estructuras, y se usa frecuentemente en machine learning y deep learning, donde suelen emplearse tensores para manejar datos multidimensionales.
"""

import numpy as np

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# CREACION DE ARRAYS CON NUMPY
# Creación de un ndarray en NumPy usando la función array()
lista1 = [1, 2, 3, 4, 5]
arr = np.array(lista1)

print("NumPy se utiliza para trabajar con arreglos (arrays). El objeto de arreglo en NumPy se llama ndarray.")
print(f"Lista en Python: {lista1}, tipo de dato: {type(lista1)}")
print(f"Arreglo de NumPy: {arr}, tipo de dato: {type(arr)}\n")

# Crear un arreglo desde una tupla o lista
tuple1 = (1, 2, 3, 4, 5)
arr = np.array(tuple1)

print("Es posible crear un arreglo a partir de una lista, tupla u otro objeto similar a un arreglo.")
print(f"Tupla en Python: {tuple1}, tipo de dato: {type(tuple1)}")
print(f"Arreglo de NumPy: {arr}, tipo de dato: {type(arr)}\n")

# Ejemplo de arreglo 0-D (escalares)
arr = np.array(42)
print("Los arreglos 0-D o escalares son los elementos individuales en un arreglo.")
print(f"Ejemplo de arreglo 0-D: {arr}\n")

# Ejemplo de arreglo 1-D (vector)
arr = np.array([1, 2, 3, 4, 5])
print("Un arreglo que contiene arreglos 0-D se llama arreglo unidimensional o 1-D (vector)")
print(f"Ejemplo de arreglo 1-D: {arr}\n")

# Ejemplo de arreglo 2-D (matriz)
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Un arreglo que contiene arreglos 1-D se llama arreglo 2-D o matriz.")
print(f"Ejemplo de matriz (arreglo 2-D):\n{arr}\n")

# Ejemplo de arreglo 3-D (tensor)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Un arreglo que contiene arreglos 2-D se llama arreglo 3-D o tensor.")
print(f"Ejemplo de tensor (arreglo 3-D):\n{arr}\n")

# Arreglos de dimensiones superiores
arr = np.array([1, 2, 3, 4], ndmin=4)
print("Un arreglo puede tener cualquier cantidad de dimensiones, utilizando el argumento ndmin.")
print(f"Ejemplo de un arreglo de 4 dimensiones:\n{arr}\n")

# Obtener el número de dimensiones de un arreglo
arr = np.array(
    [
        [[1, 2], [3, 4], [5, 6]], 
        [[7, 8], [9, 10], [11, 12]]
    ]
)
print("Ejemplo: Comprobando el número de dimensiones de un arreglo.")
print(f"El arreglo:\n{arr}\n tiene {arr.ndim} dimensiones.\n")


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# ACCEDIENDO A ELEMENTOS DE UN ARREGLO
# # La indexación en NumPy es similar a la de las listas de Python.
# Se accede a un elemento de un arreglo mediante su número de índice.
# Los índices de los arreglos de NumPy comienzan en 0, por lo que el primer elemento tiene índice 0, el segundo índice 1, y así sucesivamente.

arr = np.array([1, 2, 3, 4])

print("Es posible acceder a un elemento de un arreglo de NumPy mediante la indexación.")
print("Ejemplo: Accediendo al primer elemento del arreglo:")
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
print("Ejemplo 1: Accediendo al segundo elemento de la primera fila del arreglo:")
print(arr2D)
print(f"Elemento obtenido: {arr2D[0, 1]}\n")

# Acceso a matrices 3D
# En una matriz 3D, se usan tres índices: el primero para la profundidad, el segundo para la fila, y el tercero para la columna.
arr3D = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("Ejemplo 2: Accediendo al segundo elemento del segundo arreglo dentro del primer arreglo en una matriz 3D:")
print(arr3D)
print(f"Elemento obtenido: {arr3D[0, 1, 1]}\n")

# Indexación negativa
# Para acceder a un arreglo desde el final hacia adelante, es posible utilizar la indexación negativa.
# El índice -1 representa el último elemento, -2 el penúltimo, y así sucesivamente.
print("Para acceder a elementos de un arreglo desde el final hacia adelante, se utiliza la indexación negativa.")
print("Ejemplo: Accediendo al penúltimo elemento de la primera fila de una matriz 2D:")
print(arr2D)
print(f"Elemento obtenido: {arr2D[0, -2]}\n")

