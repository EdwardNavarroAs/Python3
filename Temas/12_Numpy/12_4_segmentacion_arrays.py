# Segmentación de arreglos
# Segmentar en Python significa tomar elementos de un índice dado a otro índice dado.
# La segmentación se realiza con la sintaxis: [inicio:fin].
# También se puede definir el paso con la sintaxis: [inicio:fin:paso].
# Si no se pasa el inicio, se considera 0.
# Si no se pasa el fin, se considera la longitud del arreglo en esa dimensión.
# Si no se pasa el paso, se considera 1.
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print("Segmentación de arreglos en NumPy")
print("Segmentar significa tomar elementos de un índice dado a otro índice dado, mediante la sintaxis: [inicio:fin]")
print("Ejemplo 1: Segmentando un arreglo 1D desde el índice 1 (incluido) hasta el índice 5 (no incluido):")
print(arr)
print(f"Arreglo segmentado: {arr[1:5]}\n")

print("Ejemplo 2: Segmentando un arreglo 1D desde el índice 5 (incluido) hasta el final:")
print(arr)
print(f"Arreglo segmentado: {arr[5:]}\n")

print("Ejemplo 3: Segmentando un arreglo 1D desde el principio hasta el índice 5 (no incluido):")
print(arr)
print(f"Arreglo segmentado: {arr[:5]}\n")

# Segmentación negativa
# Es posible segmentar un arreglo utilizando índices negativos para contar desde el final.
print("También es posible segmentar un arreglo utilizando índices negativos para contar desde el final.")
print("Ejemplo 4: Segmentando un arreglo desde el tercer índice desde el final (incluido) hasta el último índice (no incluido):")
print(arr)
print(f"Arreglo segmentado: {arr[-3:-1]}\n")

# Segmentación con paso
# Se puede utilizar un valor de paso para determinar el intervalo entre elementos en la segmentación.
print("También se puede segmentar un arreglo utilizando un valor de paso.")
print("Ejemplo 5: Segmentando un arreglo desde el índice 1 (incluido) hasta el índice 5 (no incluido) con un paso de 2:")
print(arr)
print(f"Arreglo segmentado: {arr[1:5:2]}\n")

# Segmentación de arreglos 2D
# En NumPy, la segmentación de un arreglo 2D se realiza con la sintaxis:
# arr2D[inicio_filas:fin_filas, inicio_columnas:fin_columnas]
# - `inicio_filas:fin_filas` selecciona las filas desde `inicio_filas` hasta `fin_filas` (sin incluir `fin_filas`).
# - `inicio_columnas:fin_columnas` selecciona las columnas desde `inicio_columnas` hasta `fin_columnas` (sin incluir `fin_columnas`).

arr2D = np.array([[1, 2, 3, 4, 5, 6, 7],
                  [8, 9, 10, 11, 12, 13, 14]])

print("Segmentación de arreglos 2D en NumPy")
# Explicación de la sintaxis
print("Explicación de la sintaxis:")
print("Para segmentar un arreglo 2D, se utiliza la estructura arr2D[inicio_filas:fin_filas, inicio_columnas:fin_columnas].")
print("El índice `inicio` está incluido, pero el `fin` no lo está.\n")

# Ejemplo 1: Segmentando desde la fila 1 hasta el final y columnas desde 1 hasta 4 (sin incluir 4)
print("Ejemplo 6: Segmentando desde la fila 1 hasta el final y columnas desde 1 hasta 4 (sin incluir 4):")
print(arr2D)
print(f"Arreglo segmentado:\n{arr2D[1:, 1:4]}\n")

# Ejemplo 2: Segmentando todas las filas y seleccionando columnas de índice 1 a 3
print("Ejemplo 7: Segmentando todas las filas y seleccionando columnas de índice 1 a 3:")
print(arr2D)
print(f"Arreglo segmentado:\n{arr2D[:, 1:4]}\n")

# Ejemplo 3: Segmentando la primera fila y columnas desde el índice 2 hasta el 5 (sin incluir 5)
print("Ejemplo 8: Segmentando la primera fila y columnas desde el índice 2 hasta el 5 (sin incluir 5):")
print(arr2D)
print(f"Arreglo segmentado:\n{arr2D[0, 2:5]}\n")

# Ejemplo 4: Segmentando la segunda fila con un paso de 2 en las columnas
print("Ejemplo 9: Segmentando la segunda fila con un paso de 2 en las columnas:")
print(arr2D)
print(f"Arreglo segmentado:\n{arr2D[1, ::2]}\n")
