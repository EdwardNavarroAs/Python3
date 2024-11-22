# Unión de arreglos NumPy
# Unir significa combinar el contenido de dos o más arreglos en un único arreglo.
# Por ejemplo, en SQL se unen tablas en función de una clave, mientras que en NumPy se unen arreglos a lo largo de un eje.
# Para ello se utiliza la función concatenate(), que recibe los arreglos que se desean unir junto con el eje (`axis`) que determina cómo se realiza la unión.
# Nota: Si el parámetro `axis` no se pasa explícitamente, se toma 0 por defecto (se unen filas o arreglos unidimensionales).

import numpy as np

print("Unión de arreglos NumPy")
print("Para unir dos arreglos NumPy se utiliza la función concatenate(), que une los arreglos a lo largo de un eje.")

# Ejemplo 1: Uniendo arreglos unidimensionales
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Ejemplo 1: Uniendo dos arreglos unidimensionales:")
print(f"Arreglo 1: {arr1}")
print(f"Arreglo 2: {arr2}")

arr = np.concatenate((arr1, arr2))
print(f"Resultado: \n{arr}\n")

# Ejemplo 2: Uniendo arreglos bidimensionales
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print("Ejemplo 2: Uniendo dos arreglos bidimensionales a lo largo del eje 1 (columnas):")
print(f"Arreglo 1: \n{arr1}")
print(f"Arreglo 2: \n{arr2}")

arr = np.concatenate((arr1, arr2), axis=1)  # Se unen a lo largo del eje 1 (columnas)
print(f"Resultado: \n{arr}\n")

# ¿Qué significa axis?
# - `axis=0`: Se unen a lo largo de las filas (por defecto).
# - `axis=1`: Se unen a lo largo de las columnas.
# Nota: Para unir arreglos, sus formas deben ser compatibles en el eje que no se especifica.

# Uniendo arreglos mediante funciones de pila
# El apilamiento es lo mismo que la concatenación, la única diferencia es que el apilamiento se realiza a lo largo de un nuevo eje.
print("Tambien es posible utilizar el método stack() para unir dos o más arreglos de numpy a lo largo de un eje.")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Ejemplo 3: Uniendo dos arreglos unidimensionales usando axis=1:")
print(f"Arreglo 1: {arr1}")
print(f"Arreglo 2: {arr2}")

arr = np.stack((arr1, arr2), axis=1)
print(f"Resultado: \n{arr}\n")

# Ejemplo adicional con stack para arreglos bidimensionales
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print("Ejemplo adicional: Usando stack para unir arreglos bidimensionales a lo largo de un nuevo eje:")
print(f"Arreglo 1: \n{arr1}")
print(f"Arreglo 2: \n{arr2}")
arr = np.stack((arr1, arr2), axis=2)  # Nuevo eje agregado en profundidad
print(f"Resultado: \n{arr}\n")

# Apilamiento a lo largo de filas
print("Para apilar arreglos de numpy a lo largo de filas se utiliza la función auxiliar hstack():")
print("Ejemplo 4: Apilando dos arreglos unidimensionales a lo largo de sus filas:")
print(f"Arreglo 1: {arr1}")
print(f"Arreglo 2: {arr2}")

arr = np.hstack((arr1, arr2))
print(f"Resultado: \n{arr}\n")

# Apilamiento a lo largo de columnas
print("Para apilar arreglos de numpy a lo largo de columnas se utiliza la función auxiliar vstack():")
print("Ejemplo 5: Apilando dos arreglos unidimensionales a lo largo de sus columnas:")
print(f"Arreglo 1: {arr1}")
print(f"Arreglo 2: {arr2}")

arr = np.vstack((arr1, arr2))
print(f"Resultado: \n{arr}\n")

# Apilamiento a lo largo de la altura (profundidad)
print("Para apilar arreglos de numpy a lo largo de su profundidad se utiliza la función auxiliar dstack():")
print("Ejemplo 6: Apilando dos arreglos unidimensionales a lo largo de su profundidad:")
print(f"Arreglo 1: {arr1}")
print(f"Arreglo 2: {arr2}")

arr = np.dstack((arr1, arr2))
print(f"Resultado: \n{arr}\n")

# Ejemplo adicional con dstack para arreglos bidimensionales
print("Ejemplo adicional: Apilando arreglos bidimensionales a lo largo de su profundidad:")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(f"Arreglo 1: \n{arr1}")
print(f"Arreglo 2: \n{arr2}")
arr = np.dstack((arr1, arr2))
print(f"Resultado: \n{arr}\n")

# División de arreglos en NumPy
# Unir fusiona varios arreglos en uno solo, mientras que dividir separa un arreglo en varios.
# La función array_split() permite dividir un arreglo de NumPy. Recibe el arreglo que se desea dividir junto con la cantidad de divisiones.
# Nota: El resultado de la función array_split() es una lista de arreglos de NumPy.

print("División de arreglos NumPy")
print("Para dividir un arreglo NumPy se utiliza la función array_split().")

# Ejemplo 1: Dividiendo un arreglo unidimensional
arr = np.array([1, 2, 3, 4, 5, 6])
print("\nEjemplo 1: Dividiendo un arreglo unidimensional en 3 partes:")
print(arr)
newarr = np.array_split(arr, 3)
print(f"Resultado: \n{newarr}\n")
# Nota: Cada subarreglo tiene aproximadamente la misma cantidad de elementos, pero si no es divisible exactamente, se ajustan los tamaños.

# Ejemplo 2: División con ajuste automático
# Si el arreglo tiene menos elementos de los necesarios, entonces la función ajustará el resultado desde el final en consecuencia.
# Nota: La función split() no ajusta automáticamente, mientras que array_split() sí lo hace.
print("Ejemplo 2: Dividiendo un arreglo unidimensional en 4 partes (ajuste automático):")
print(arr)
newarr = np.array_split(arr, 4)
print(f"Resultado: \n{newarr}\n")

# Ejemplo 3: Accediendo a los elementos divididos
# El valor que retorna array_split() es una lista de arreglos. Es posible acceder a cada uno como a cualquier elemento de una lista.
print("Ejemplo 3: Accediendo a los valores de las divisiones:")
print(arr)
newarr = np.array_split(arr, 3)
print(f"El segundo resultado de la división es: \n{newarr[1]}\n")

# División de arreglos 2D
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print("Ejemplo 4: Dividiendo un arreglo bidimensional en 3 partes (a lo largo de filas, por defecto):")
print(arr)
newarr = np.array_split(arr, 3)
print(f"Resultado: \n{newarr}\n")

# Ejemplo 5: Dividiendo un arreglo bidimensional a lo largo de las columnas
# Es posible especificar el eje de división mediante el parámetro axis.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print("Ejemplo 5: Dividiendo un arreglo bidimensional en 3 partes a lo largo de sus columnas (axis=1):")
print(arr)
newarr = np.array_split(arr, 3, axis=1)
print(f"Resultado: \n{newarr}\n")

# Ejemplo 6: Usando hsplit() para dividir a lo largo de las columnas
# hsplit() es una función auxiliar para dividir arreglos específicamente a lo largo de las columnas (axis=1).
print("Ejemplo 6: Dividiendo un arreglo bidimensional en 3 partes a lo largo de sus columnas utilizando hsplit():")
print(arr)
newarr2 = np.hsplit(arr, 3)
print(f"Resultado: \n{newarr2}\n")

# Ejemplo 7: Usando vsplit() para dividir a lo largo de las filas
# vsplit() es una función auxiliar para dividir arreglos específicamente a lo largo de las filas (axis=0).
print("Ejemplo 7: Dividiendo un arreglo bidimensional en 3 partes a lo largo de sus filas utilizando vsplit():")
newarr3 = np.vsplit(arr, 3)
print(f"Resultado: \n{newarr3}\n")

# Ejemplo 8: División de un arreglo tridimensional
# En arreglos multidimensionales, se puede especificar el eje para dividir.
arr3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]], [[13, 14], [15, 16]]])
print("Ejemplo 8: Dividiendo un arreglo tridimensional en 2 partes a lo largo de su profundidad (axis=0):")
print(arr3D)
newarr4 = np.array_split(arr3D, 2, axis=0)
print(f"Resultado: \n{newarr4}\n")
