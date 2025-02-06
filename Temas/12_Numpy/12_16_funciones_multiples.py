"""
**Funciones Universales en NumPy (ufuncs)**
Las **ufuncs** (Universal Functions) son funciones optimizadas que operan sobre arreglos (`ndarray`) en NumPy.

**Ventajas de las ufuncs**:
1. **Vectorización**: Permiten realizar operaciones sobre arreglos completos sin necesidad de bucles (`for`), lo que mejora el rendimiento.
2. **Optimización**: Internamente están implementadas en **C**, lo que las hace mucho más rápidas que las operaciones tradicionales en Python.
3. **Soporte para transmisión de dimensiones (`broadcasting`)**: Pueden operar en arreglos de diferentes formas sin necesidad de reescalar manualmente.
4. **Funciones adicionales**: Incluyen operaciones de reducción (`reduce`), acumulación (`accumulate`), etc.

**Parámetros importantes en ufuncs**:
Las ufuncs aceptan argumentos adicionales que controlan su comportamiento:
- `where`: Define una condición para que la operación se aplique solo en ciertos elementos.
- `dtype`: Permite especificar el tipo de dato del resultado.
- `out`: Define un arreglo de salida donde se almacenará el resultado.
"""
import numpy as np

# **Vectorización**
# Convertir operaciones iterativas en operaciones basadas en vectores se denomina **vectorización**.
# Esto es más rápido porque las CPU modernas están optimizadas para operaciones vectorizadas.

print("Vectorización en NumPy: Convertir bucles en operaciones con arreglos.")
print("Ejemplo 1: Sumando los elementos de dos listas usando `zip()` en Python.")

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = [i + j for i, j in zip(x, y)]

print(f"Resultado: {z}, tipo de dato: {type(z)}")
print('')

# **Uso de la ufunc `add()` en NumPy**
print("Ejemplo 2: Sumando listas utilizando `np.add()`")

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(f"Resultado: {z}, tipo de dato: {type(z)}")
print('')

# **Crear una ufunc propia con `frompyfunc()`**
print("Ejemplo 3: Creando una ufunc propia con `frompyfunc()`")

def myadd(x, y):
    return x + y

myadd_ufunc = np.frompyfunc(myadd, 2, 1)
z = myadd_ufunc(x, y)

print(f"Resultado: {z}, tipo de dato: {type(z)}")
print('')

# **Verificar si una función es una ufunc**
print("Ejemplo 4: Verificando si `np.add` es una ufunc.")
if isinstance(np.add, np.ufunc):
    print('`np.add` es una función ufunc.')
else:
    print('`np.add` no es una función ufunc.')
print('')

# **Operaciones aritméticas con ufuncs**
print("OPERACIONES UFUNC PARA ARITMÉTICA BÁSICA")

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

# **Suma**
print("Ejemplo: Suma de arreglos")
print(f"Resultado: {np.add(arr1, arr2)}\n")

# **Resta**
print("Ejemplo: Resta de arreglos")
print(f"Resultado: {np.subtract(arr1, arr2)}\n")

# **Multiplicación**
print("Ejemplo: Multiplicación de arreglos")
print(f"Resultado: {np.multiply(arr1, arr2)}\n")

# **División**
print("Ejemplo: División de arreglos")
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
print(f"Resultado: {np.divide(arr1, arr2)}\n")

# **Potenciación**
print("Ejemplo: Potencias con `np.power()`")
arr1 = np.array([2, 3, 4, 5])
arr2 = np.array([3, 2, 1, 0])
print(f"Resultado: {np.power(arr1, arr2)}\n")

# **Residuo**
print("Ejemplo: Residuo de división con `np.mod()` y `np.remainder()`")
print(f"Con `np.mod()`: {np.mod(arr1, arr2)}")
print(f"Con `np.remainder()`: {np.remainder(arr1, arr2)}\n")

# **Cociente y módulo**
print("Ejemplo: `divmod()` devuelve el cociente y el residuo de la división")
cociente, residuo = np.divmod(arr1, arr2)
print(f"Cociente: {cociente}")
print(f"Residuo: {residuo}\n")

# **Valor absoluto**
print("Ejemplo: Valor absoluto de un arreglo con `np.absolute()`")
arr = np.array([-1, -2, 1, 2, 3, -4])
print(f"Resultado: {np.absolute(arr)}\n")
