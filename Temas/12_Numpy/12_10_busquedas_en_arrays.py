# Búsqueda en arreglos de numpy
# numpy permite buscar un valor determinado en un arreglo y devolver los índices que coincidan con la busqueda.
# Para ello se utiliza el método where().
import numpy as np

print("Busqueda en arreglos de numpy")
print("numpy permite buscar un valor determinado en un arreglo y devolver los índices que coincidan con la busqueda.")
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)
