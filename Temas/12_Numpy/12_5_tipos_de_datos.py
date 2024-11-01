# Tipos de datos en NumPy
# NumPy tiene tipos de datos adicionales y los representa con caracteres específicos como 'i' para números enteros, 'u' para enteros sin signo, etc.
# Lista de tipos de datos en NumPy y sus caracteres de representación:

"""
Tipos de datos en NumPy:
i - integer (entero)
b - boolean (booleano)
u - unsigned integer (entero sin signo)
f - float (flotante)
c - complex float (número complejo)
m - timedelta (intervalo de tiempo)
M - datetime (fecha y hora)
O - object (objeto genérico de Python)
S - string (cadena de caracteres)
U - unicode string (cadena de caracteres Unicode)
V - fixed chunk of memory for other type (void - espacio de memoria fijo)
"""

# Comprobación del tipo de datos de un arreglo en NumPy
# Todos los arreglos de NumPy tienen una propiedad llamada dtype que devuelve el tipo de datos del arreglo.
import numpy as np

arr = np.array([1, 2, 3, 4])
print("Comprobación del tipo de datos de un arreglo en NumPy")
print("Todos los arreglos de NumPy tienen una propiedad llamada dtype que devuelve el tipo de datos del arreglo.")
print("Ejemplo 1: Obteniendo el tipo de datos del arreglo:")
print(arr)
print(f"Resultado: {arr.dtype} \n")

arr = np.array(['apple', 'banana', 'cherry'])
print("Ejemplo 2: Obteniendo el tipo de datos del arreglo:")
print(arr)
print(f"Resultado: {arr.dtype} \n")

# Creación de arreglos con un tipo de datos definido
# Para crear un arreglo con un tipo de dato específico, se utiliza la función array() con el argumento dtype.
print("Creación de arreglos con un tipo de datos definido")
print("Para crear un arreglo con un tipo de dato definido se utiliza la función array() con el argumento dtype.")
data = [1, 2, 3, 4]
arr = np.array(data, dtype='S')  # 'S' crea un arreglo de tipo string de bytes.

print(f"Ejemplo 3: Creando un arreglo de tipo string a partir de los datos: {data}")
print(f"Resultado: \n{arr}\n cuyo tipo de dato es: {arr.dtype} \n")

# Definición de tamaño para tipos como i, u, f, S y U
arr2 = np.array(data, dtype='i4')  # 'i4' significa entero de 4 bytes (32 bits)
print(f"Ejemplo 4: Creando un arreglo de tipo entero de 4 bytes a partir de los datos: {data}")
print(f"Resultado: \n{arr2}\n cuyo tipo de dato es: {arr2.dtype} \n")

# Manejo de errores al intentar convertir tipos no compatibles
# Si no se puede convertir un valor, NumPy generará un error.
# arr = np.array(['a', '2', '3'], dtype='i')  # Esto fallará porque 'a' no es convertible a entero.

# Conversión del tipo de datos en arreglos existentes
# La mejor forma de cambiar el tipo de datos de un arreglo existente es hacer una copia del arreglo con el método astype().
# La función astype() crea una copia del arreglo y permite especificar el tipo de datos como parámetro.
arr = np.array([1.1, 2.1, 0])

print("Conversión del tipo de datos en arreglos existentes")
print("La mejor forma de cambiar el tipo de datos de un arreglo existente es hacer una copia con el método astype().")
newarr = arr.astype('i')  # Convierte a entero
# También se puede utilizar el tipo de dato de forma explícita como parámetro en la función astype()
newarr2 = arr.astype(bool)  # Convierte a booleano

print(f"Ejemplo 5: Convirtiendo a entero los tipos de datos del arreglo: {arr}")
print(f"Resultado: \n{newarr}\n cuyo tipo de dato es: {newarr.dtype} \n")

print(f"Ejemplo 6: Convirtiendo a booleano los tipos de datos del arreglo: {arr}")
print(f"Resultado: \n{newarr2}\n cuyo tipo de dato es: {newarr2.dtype} \n")
