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
