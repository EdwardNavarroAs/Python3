# Filtrado de arreglos en NumPy
# El proceso de extraer algunos elementos de un arreglo existente y crear un nuevo arreglo a partir de ellos se denomina filtrado.
# En NumPy, se filtra un arreglo mediante una lista de índices booleanos.
# Una lista de índices booleanos es una lista de valores booleanos que corresponden a los índices del arreglo.
# Si el valor de un índice es True, ese elemento está incluido en el arreglo filtrado; si el valor de ese índice es False, ese elemento se excluye del arreglo filtrado.

import numpy as np

print("Filtrado de arreglos en NumPy")
print("En NumPy, se filtra un arreglo mediante una lista de índices booleanos. Si el valor de un índice es True, ese elemento está incluido en el arreglo filtrado; si el valor de ese índice es False, ese elemento se excluye del arreglo filtrado.")

# Ejemplo 1: Filtrado básico con una lista de índices booleanos
print("\nEjemplo 1: Filtrando un arreglo unidimensional usando índices booleanos:")
arr = np.array([41, 42, 43, 44])
print("Arreglo original:")
print(arr)
print("Lista de índices booleanos:")
x = [True, False, True, False]
print(x)
newarr = arr[x]
print("Arreglo filtrado:")
print(newarr)
print('')

# Ejemplo 2: Creando un filtro basado en una condición
print("Ejemplo 2: Creando un filtro que devuelve solo valores mayores a 42:")
arr = np.array([41, 42, 43, 44])
print("Arreglo original:")
print(arr)

# Crear un filtro utilizando una comprensión de listas
filter_arr = [True if element > 42 else False for element in arr]
print("Arreglo de filtros:")
print(filter_arr)
newarr = arr[filter_arr]
print("Arreglo filtrado:")
print(newarr)
print('')

# Ejemplo 3: Creando un filtro para valores pares
print("Ejemplo 3: Creando un filtro que devuelve solo los valores pares:")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Arreglo original:")
print(arr)

# Crear un filtro utilizando una comprensión de listas
filter_arr = [True if element % 2 == 0 else False for element in arr]
print("Arreglo de filtros:")
print(filter_arr)
newarr = arr[filter_arr]
print("Arreglo filtrado:")
print(newarr)
print('')

# Ejemplo 4: Filtrado directo con NumPy
# NumPy permite aplicar condiciones directamente sobre el arreglo para crear filtros más eficientes.
print("Ejemplo 4: Filtrando directamente los valores mayores a 42 en un arreglo:")
arr = np.array([41, 42, 43, 44])
print("Arreglo original:")
print(arr)

# Crear un filtro directamente desde el arreglo
filter_arr = arr > 42
print("Arreglo de filtros:")
print(filter_arr)
newarr = arr[filter_arr]
print("Arreglo filtrado:")
print(newarr)
print('')

# Ejemplo 5: Filtrado directo para valores pares
print("Ejemplo 5: Filtrando directamente los valores pares en un arreglo:")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Arreglo original:")
print(arr)

# Crear un filtro directamente desde el arreglo
filter_arr = arr % 2 == 0
print("Arreglo de filtros:")
print(filter_arr)
newarr = arr[filter_arr]
print("Arreglo filtrado:")
print(newarr)
print('')

# Ejemplo adicional: Filtrando un arreglo bidimensional
print("Ejemplo adicional: Filtrando un arreglo bidimensional para valores mayores a 5:")
arr = np.array([[1, 6, 3], [8, 2, 9]])
print("Arreglo original:")
print(arr)

# Crear un filtro directamente desde el arreglo
filter_arr = arr > 5
print("Arreglo de filtros:")
print(filter_arr)
newarr = arr[filter_arr]
print("Arreglo filtrado:")
print(newarr)
print('')
