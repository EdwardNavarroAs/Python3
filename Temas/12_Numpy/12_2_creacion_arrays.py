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
