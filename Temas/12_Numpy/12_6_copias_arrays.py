# La diferencia entre copia y vista
# La principal diferencia entre una copia y una vista de un arreglo es que la copia es un nuevo arreglo independiente, 
# mientras que la vista es solo una representación de los datos del arreglo original.
# Una copia es propietaria de los datos, por lo que cualquier cambio realizado en la copia no afectará al arreglo original, y viceversa.
# Una vista no es propietaria de los datos; cualquier cambio realizado en la vista afectará al arreglo original, y viceversa.

import numpy as np

print("Una copia de un arreglo permite realizar cambios sobre la copia sin afectar al arreglo original.")
print("Ejemplo 1: Copia de un arreglo")
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
print(f"Arreglo original: {arr}")
print(f"Copia del arreglo: {x}")
x[0] = 42  # Modificamos la copia
print(f"Copia modificada: {x}")
print(f"Arreglo original sin cambios: {arr}\n")  # La copia modificada no afecta al original

print("Una vista de un arreglo no es propietaria de los datos; cualquier cambio en la vista también afectará al arreglo original.")
print("Ejemplo 2: Vista de un arreglo")
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
print(f"Arreglo original: {arr}")
print(f"Vista del arreglo: {x}")
x[3] = 21  # Modificamos la vista
print(f"Vista modificada: {x}")
print(f"Arreglo original afectado por el cambio en la vista: {arr}\n")  # La vista modificada afecta al original

# Comprobar si un arreglo es propietario de sus datos
# Como se mencionó, las copias son propietarias de los datos, mientras que las vistas no.
# Para comprobarlo, cada arreglo de NumPy tiene el atributo `base`, que devuelve `None` si el arreglo es propietario de sus datos.
# De lo contrario, el atributo `base` hace referencia al objeto original en caso de que el arreglo sea una vista.

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()
print("Comprobación de propiedad de datos en un arreglo utilizando el atributo 'base'")
print("El atributo 'base' devuelve None si el arreglo es propietario de los datos.")
print("Si el arreglo es una vista, el atributo 'base' referencia al arreglo original.")
print(f"Arreglo original: {arr}")
print(f"Copia del arreglo: {x}")
print(f"Vista del arreglo: {y}")

# Verificación de propiedad de datos
print(f"¿La copia del arreglo es propietaria de los datos? (None significa que sí): {x.base}")
print(f"¿La vista del arreglo es propietaria de los datos? (Referencia al arreglo original si es una vista): {y.base}\n")
