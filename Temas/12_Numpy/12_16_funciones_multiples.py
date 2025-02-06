"""
ufuncs significa "Funciones universales" y son funciones NumPy que operan sobre el ndarrayobjeto.

Las ufuncs se utilizan para implementar la vectorización en NumPy, lo cual es mucho más rápido que iterar sobre elementos.

También proporcionan transmisión y métodos adicionales como reducción, acumulación, etc., que son muy útiles para el cálculo.

Las ufuncs también aceptan argumentos adicionales, como:

    - where: arreglo booleano o condición que define dónde deben realizarse las operaciones.
    - dtype: definir el tipo de retorno de los elementos.
    - out: arreglo de salida donde se debe copiar el valor de retorno.
    
"""
import numpy as np

# vectorización
# La conversión de declaraciones iterativas en una operación basada en vectores se denomina vectorización.
# Es más rápido porque las CPU modernas están optimizadas para tales operaciones.

print("la vectorizacion en numpy se denomina al proceso de conversion de declaraciones iterativas en una operación basada en vectores ")
print("por ejemplo en python es posible realizar la suma de los elementos de las listas utilizando en metodo zip()")

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = [i+j for i,j in zip(x, y)]

print(f"Ejemplo 1: Sumando los elementos de las listas: {x} y {y} utilizando el metodo zip()")
print(f"resultado: {z}, tipo de dato: {type(z)}")
print('')

# sin embargo NumPy tiene una ufunc para esto, llamada add(x, y) que produce el mismo resultado pero optimizado.
print("NumPy tiene la ufunc add(x,y) que realiza el mismo procedimiento anterior de manera optimizada.")

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(f"Ejemplo 2: Sumando los elementos de las listas: {x} y {y} utilizando la ufunc de numpy add()")
print(f"resultado: {z}, tipo de dato: {type(z)}")
print('')

"""
En Numpy es posible crear una ufunc propia.
Para crear una ufunc propia, se debe definir una función normal de python, y luego agregar dicha funcion a la biblioteca de ufunc de NumPy con el método frompyfunc().

El método frompyfunc() tiene los siguientes argumentos:

    - function: nombre de la función.
    - inputs: cantidad de argumentos de entrada (arreglos).
    - outputs: cantidad de arreglos de salida.
"""

print("En Numpy es posible crear una ufunc propia utilizando el método frompyfunc().")
def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)
z = myadd(x, y)

print(f"Ejemplo 3: Sumando los elementos de las listas: {x} y {y} utilizando una ufunc propia creada utilizando el metodo frompyfunc()")
print(f"resultado: {z}, tipo de dato: {type(z)}")
print('')

# Para comprobar si una función es una ufunc se utiliza el metodo type () de python
print("Para verificar si una funcion es del tipo unfunc se debe utilizar el metodo type() de python")
print(f"Ejemplo 4: verificando si la funcion add de numpy es del typo unfunc")
if type(np.add) == np.ufunc:
  print('add es del tipo ufunc')
else:
  print('add no es una funcion del tipo ufunc')
print('')

