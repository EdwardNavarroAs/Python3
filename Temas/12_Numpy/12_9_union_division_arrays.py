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
