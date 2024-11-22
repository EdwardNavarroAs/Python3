# Búsqueda en arreglos de NumPy
# NumPy permite buscar un valor determinado en un arreglo y devolver los índices que coincidan con la búsqueda.
# Para ello se utiliza el método where().

import numpy as np

print("Búsqueda en arreglos de NumPy")

# Búsqueda con el método where()
print("NumPy permite buscar un valor determinado en un arreglo y devolver los índices que coincidan con la búsqueda.")
arr = np.array([1, 2, 3, 4, 5, 4, 4])
print("\nEjemplo 1: Buscando los índices que pertenecen al valor '4' en el arreglo:")
print(arr)
x = np.where(arr == 4)
print(f"Resultado: \n{x}\n")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Ejemplo 2: Buscando los índices que pertenecen a los valores pares en el arreglo:")
print(arr)
x = np.where(arr % 2 == 0)
print(f"Resultado: \n{x}\n")

print("Ejemplo 3: Buscando los índices que pertenecen a los valores impares en el arreglo:")
print(arr)
x = np.where(arr % 2 == 1)
print(f"Resultado: \n{x}\n")

# Búsqueda ordenada con searchsorted()
# El método searchsorted() realiza una búsqueda binaria en un arreglo y devuelve el índice donde se debe insertar el valor especificado para mantener el orden del arreglo.
# Nota: Se supone que el método searchsorted() se utiliza en arreglos ordenados. 
print("El método searchsorted() realiza una búsqueda binaria y devuelve el índice donde se debe insertar un valor para mantener el orden del arreglo.")

arr = np.array([6, 7, 8, 9])
print("\nEjemplo 4: Encontrando el índice donde se debe insertar el valor 7 en el arreglo:")
print(arr)
x = np.searchsorted(arr, 7)
print(f"Resultado: \n{x}\n")

print("Ejemplo 5: Encontrando el índice donde se debe insertar el valor 7 comenzando la búsqueda desde la derecha:")
print(arr)
x = np.searchsorted(arr, 7, side="right")
print(f"Resultado: \n{x}\n")

# Búsqueda de múltiples valores con searchsorted()
# Para buscar múltiples valores, se pasa un arreglo con los valores deseados.
arr = np.array([1, 3, 5, 7])
print("Ejemplo 6: Encontrando los índices donde se deben insertar los valores [2, 4, 6] en el arreglo:")
print(arr)
x = np.searchsorted(arr, [2, 4, 6])
print(f"Resultado: \n{x}\n")

# Ejemplo adicional: Insertar valores menores o mayores al rango del arreglo
print("Ejemplo 7: Insertando valores fuera del rango del arreglo:")
arr = np.array([10, 20, 30, 40, 50])
print(arr)
x = np.searchsorted(arr, [5, 55])
print(f"Resultado: \n{x}\n")

# Ejemplo adicional: Usando searchsorted() en un arreglo descendente
print("Ejemplo 8: Usando searchsorted() en un arreglo descendente:")
arr = np.array([50, 40, 30, 20, 10])
print(arr)
x = np.searchsorted(arr[::-1], [35, 45])  # Revierto el arreglo para que sea ordenado ascendentemente
print(f"Resultado: \n{x}\n")
