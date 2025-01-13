#¿Qué es la distribución de datos?
# La distribución de datos es una lista de todos los valores posibles y la frecuencia con la que se produce cada valor.

"""
Estas listas son importantes cuando se trabaja con estadísticas y ciencia de datos.

El módulo random de numpy ofrece métodos que devuelven distribuciones de datos generadas aleatoriamente.

Conceptos importantes
- Distribución aleatoria:
    Una distribución aleatoria es un conjunto de números aleatorios que siguen una determinada función de densidad de probabilidad.

- Función de densidad de probabilidad: 
    función que describe una probabilidad continua, es decir, la probabilidad de todos los valores en un arreglo.
"""

#En Numpy es posible generar números aleatorios en función de probabilidades definidas mediante el método choice() del módulo random.
#El método choice() permite especificar la probabilidad de cada valor.
#La probabilidad se establece mediante un número entre 0 y 1, donde 0 significa que el valor nunca se producirá y 1 significa que el valor siempre se producirá.

from numpy import random
print("Números aleatorios a partir de distribuciones")
print("En Numpy es posible generar números aleatorios en función de probabilidades definidas mediante el método choice() del módulo random. El cual permite especificar la probabilidad de cada valor individual en el arreglo.")

# Ejemplo 1: 
# Generando un arreglo de 1-D que conteniene 100 valores, donde cada valor debe ser 3, 5, 7 o 9.
# La probabilidad de que el valor sea 3 se establece en 0.1, la probabilidad de que el valor sea 5 se establece en 0.3, la probabilidad de que el valor sea 7 se establece en 0.6, la probabilidad de que el valor sea 9 se establece en 0
print("Ejemplo 1: Generando un arreglo que contie 100 valores, donde cada valor debe ser 3, 5, 7 o 9, con un cierto nivel de probabilidad.")

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(f"Resultado: {x}")
print(f"Longitud del resultado: {len(x)}")
print('')
# Notas: 
#   - En el ejemplo anterior la suma de todas las probabilidades debe dar 1
#   - Incluso si ejecuta el ejemplo anterior 1000 veces, el valor 9 nunca aparecerá.


# Ejemplo 2: 
# Generando un arreglo de 2-D que contiene 3 filas con 5 elementos cada una (15 valores en total) , donde cada valor debe ser 3, 5, 7 o 9.
# La probabilidad de que el valor sea 3 se establece en 0.1, la probabilidad de que el valor sea 5 se establece en 0.3, la probabilidad de que el valor sea 7 se establece en 0.6, la probabilidad de que el valor sea 9 se establece en 0
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(f"Resultado: {x}")
print('')
