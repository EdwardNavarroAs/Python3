# Iteración de arreglos
# Iterar significa recorrer los elementos de un arreglo de NumPy.
# Una forma básica de hacerlo es utilizando un bucle for estándar de Python.

import numpy as np

print("Iteración de arreglos en NumPy")
print("Para iterar un arreglo en NumPy, se puede utilizar un bucle for estándar.")

# Ejemplo 1: Iterar un arreglo unidimensional
arr = np.array([1, 2, 3])
print(f"Ejemplo 1: Recorriendo cada elemento del siguiente arreglo unidimensional:")
print(arr)
for x in arr:
    print("Elemento del arreglo:", x)
print('')

# Ejemplo 2: Iterar un arreglo bidimensional (fila por fila)
arr = np.array([[1, 2, 3], [5, 6, 7]])
print(f"Ejemplo 2: Recorriendo las filas de un arreglo bidimensional:")
print(arr)
for x in arr:
    print("Fila del arreglo:", x)
print('')

# Ejemplo 3: Iterar todos los elementos de un arreglo bidimensional
print(f"Ejemplo 3: Recorriendo cada elemento del arreglo bidimensional:")
print(arr)
for row in arr:
    for element in row:
        print("Elemento del arreglo:", element)
print('')

# Ejemplo 4: Iterar todos los elementos de un arreglo tridimensional
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"Ejemplo 4: Recorriendo cada elemento de un arreglo tridimensional:")
print(arr)
for matrix in arr:
    for row in matrix:
        for element in row:
            print("Elemento del arreglo:", element)
print('')

# Iteración de arreglos con nditer()
# La función nditer() simplifica la iteración a través de arreglos multidimensionales.
# Es más eficiente para trabajar con arreglos NumPy y elimina la necesidad de anidar múltiples bucles for.
print("Iteración de arreglos con el método nditer()")
print(f"Ejemplo 1: Recorriendo cada elemento de un arreglo tridimensional usando nditer():")
print(arr)
for element in np.nditer(arr):
    print("Elemento del arreglo:", element)
print('')

# Iteración de un arreglo con diferentes tipos de datos
# Usando el argumento `op_dtypes`, se puede cambiar temporalmente el tipo de datos de los elementos durante la iteración.
# Para habilitar esto, es necesario usar `flags=['buffered']` para asignar espacio adicional en el buffer.
arr = np.array([1, 2, 3])
print("Ejemplo 2: Iteración de un arreglo con diferentes tipos de datos usando nditer():")
print(arr)
for element in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(f"Elemento del arreglo: {element}, tipo de dato del elemento: {type(element)}")
print('')

# Iteración con diferentes tamaños de pasos
# NumPy permite iterar sobre un subconjunto del arreglo aplicando un filtro o paso (stride).
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Iteración de un arreglo con diferentes tamaños de pasos usando nditer()")
print("Ejemplo 3: Iterando sobre un arreglo 2D, omitiendo elementos (stride):")
print(arr)
for element in np.nditer(arr[:, ::2]):  # Filtrar columnas alternas
    print("Elemento del arreglo:", element)
print('')

# Iteración enumerada con ndenumerate()
# El método ndenumerate() permite obtener los índices y valores de los elementos durante la iteración.
arr = np.array([1, 2, 3])
print("Iteración enumerada con ndenumerate()")
print("Ejemplo 4: Iterando y obteniendo la posición de cada elemento de un arreglo unidimensional:")
print(arr)
for index, element in np.ndenumerate(arr):
    print(f"Valor del elemento en la posición {index}: {element}")
print('')

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Ejemplo 5: Iterando y obteniendo la posición de cada elemento de un arreglo bidimensional:")
print(arr)
for index, element in np.ndenumerate(arr):
    print(f"Valor del elemento en la posición {index}: {element}")
print('')

