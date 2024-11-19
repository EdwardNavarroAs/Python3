# Forma de un arreglo
# La forma de un arreglo es la cantidad de elementos en cada dimensión.

# Obtener la forma de un arreglo
# Los arreglos de NumPy tienen un atributo llamado 'shape' que devuelve una tupla.
# Cada posición de la tupla representa una dimensión, y su valor es la cantidad de elementos en esa dimensión.
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Obtener la forma de un arreglo")
print("Todos los arreglos de NumPy tienen un atributo llamado 'shape' que devuelve una tupla con el número de elementos en cada dimensión.")
print("Ejemplo 1: Obteniendo la forma del arreglo:")
print(arr)
print(f"Resultado: {arr.shape} \n")
# En este ejemplo, el resultado (2, 4) significa que el arreglo tiene 2 dimensiones:
# - La primera dimensión (filas) tiene 2 elementos.
# - La segunda dimensión (columnas) tiene 4 elementos.

# Ejemplo con un arreglo de dimensiones superiores
arr = np.array([1, 2, 3, 4], ndmin=5)
print("Ejemplo 2: Obteniendo la forma de un arreglo con más dimensiones:")
print(arr)
print(f"Resultado: {arr.shape} \n")

# Ejemplo 3: Un arreglo 1D (una sola dimensión)
arr1D = np.array([1, 2, 3, 4, 5])
print("Ejemplo 3: Obteniendo la forma de un arreglo 1D:")
print(arr1D)
print(f"Resultado: {arr1D.shape} \n")
# En este caso, el resultado (5,) significa que el arreglo tiene solo 1 dimensión con 5 elementos.

# Ejemplo 4: Un arreglo 3D
arr3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Ejemplo 4: Obteniendo la forma de un arreglo 3D:")
print(arr3D)
print(f"Resultado: {arr3D.shape} \n")
# En este ejemplo, el resultado (2, 2, 2) significa que el arreglo tiene 3 dimensiones:
# - La primera dimensión tiene 2 matrices.
# - La segunda dimensión tiene 2 filas en cada matriz.
# - La tercera dimensión tiene 2 columnas en cada fila.

# Ejemplo 5: Un arreglo con una dimensión de longitud 1
arr_single = np.array([[[[1]]]])
print("Ejemplo 5: Obteniendo la forma de un arreglo con una dimensión de longitud 1:")
print(arr_single)
print(f"Resultado: {arr_single.shape} \n")
# En este caso, el resultado (1, 1, 1, 1) significa que el arreglo tiene 4 dimensiones:
# - La primera dimensión tiene 1 elemento.
# - La segunda dimensión tiene 1 elemento.
# - La tercera dimensión tiene 1 elemento.
# - La cuarta dimensión tiene 1 elemento.

# ¿Qué representa la tupla de forma?
# Los enteros en cada posición de la tupla indican la cantidad de elementos en la dimensión correspondiente.
# A modo de resumen:
# - (2, 4) indica 2 filas y 4 columnas.
# - (1, 1, 1, 1) indica un arreglo de 4 dimensiones con solo 1 elemento en cada dimensión.
# - (5,) indica un arreglo de una sola dimensión con 5 elementos.
# - (2, 2, 2) indica un arreglo de 3 dimensiones con 2 matrices, 2 filas y 2 columnas por cada fila..

# Redimensionando Arreglos (reshape)
# Redimensionar significa cambiar la forma de un arreglo.
# La forma de un arreglo es la cantidad de elementos en cada dimensión.
# Al redimensionar, es posible agregar o quitar dimensiones o cambiar la cantidad de elementos en cada dimensión.
# Nota: El número total de elementos en el arreglo redimensionado debe coincidir con el número total de elementos del arreglo original.
#       Redimensionar un arreglo de NumPy no modifica el arreglo original; devuelve un nuevo arreglo.

# Reshape de un arreglo 1D a un arreglo 2D
print("Redimensionando Arreglos (reshape)")
print("Al redimensionar, es posible agregar o quitar dimensiones o cambiar la cantidad de elementos en cada dimensión.")
print("Ejemplo 1: Convirtiendo un arreglo unidimensional con 12 elementos en un arreglo bidimensional con 4 arreglos, cada uno con 3 elementos:")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# En este caso, la dimensión más externa tendrá 4 matrices, cada una con 3 elementos.
newarr = arr.reshape(4, 3)
print(arr)
print(f"Resultado: \n{newarr} \n")

# Reshape de un arreglo 1D a un arreglo 3D
print("Ejemplo 2: Convirtiendo un arreglo unidimensional con 12 elementos en un arreglo tridimensional.")
print("La dimensión más externa tendrá 2 arreglos, que a su vez contienen 3 arreglos, cada uno con 2 elementos:")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(arr)
print(f"Resultado: \n{newarr} \n")

# Dimensión de un arreglo desconocida
# NumPy permite redimensionar un arreglo en una dimensión "desconocida".
# Esto significa que no es necesario especificar un número exacto para una de las dimensiones en el método reshape.
# Para ello, se utiliza el parámetro -1 como valor, lo que permite a NumPy calcular automáticamente esa dimensión.
# Nota: No es posible pasar -1 a más de una dimensión.
print("Dimensión de un arreglo desconocida")
print("NumPy permite redimensionar un arreglo en una dimensión 'desconocida', utilizando el parámetro -1 en el método reshape().")
print("Ejemplo 3: Convirtiendo un arreglo unidimensional con 8 elementos en un arreglo 3D con dimensiones 2x2x2:")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(arr)
print(f"Resultado: \n{newarr} \n")

# Aplanamiento de arreglos
# Aplanar un arreglo significa convertir un arreglo multidimensional en un arreglo unidimensional.
# Para ello, es posible utilizar el método reshape(-1).
print("Aplanamiento de un arreglo de NumPy")
print("Aplanar un arreglo significa convertir un arreglo multidimensional en un arreglo unidimensional.")
print("Ejemplo 4: Aplanando un arreglo de 2 dimensiones:")
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(arr)
print(f"Resultado: \n{newarr} \n")
