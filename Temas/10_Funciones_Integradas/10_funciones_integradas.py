# Tema 10: Funciones integradas en Python

# Python tiene muchas funciones integradas que son extremadamente útiles para tareas comunes.
# Estas funciones están disponibles de manera predeterminada y no requieren ninguna importación adicional.

# Función zip()
# La función zip() toma dos o más iterables (como listas, tuplas) y devuelve un iterador que agrega 
# elementos de los iterables proporcionados, en pares.

print("Ejemplo 1: Uso de zip() para combinar dos listas")
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
resultado = zip(lista1, lista2)
print(f"Resultado de zip(): {list(resultado)}")
print('')

# Ejemplo avanzado: Uso de zip() con tres iterables
print("Ejemplo avanzado: Uso de zip() con tres listas")
nombres = ["Ana", "Pedro", "Laura"]
edades = [23, 34, 29]
ciudades = ["Madrid", "Bogotá", "Lima"]
resultado = zip(nombres, edades, ciudades)
print(f"Resultado avanzado de zip(): {list(resultado)}")
print('')

# Función map()
# La función map() toma una función y un iterable como argumento y aplica la función a cada elemento del iterable.

print("Ejemplo 2: Uso de map() para aplicar una función a una lista")
def cuadrado(n):
    return n ** 2

numeros = [1, 2, 3, 4, 5]
resultado = map(cuadrado, numeros)
print(f"Resultado de map(): {list(resultado)}")
print('')

# Ejemplo avanzado: Uso de map() con funciones anidadas
print("Ejemplo avanzado: Uso de map() con funciones anidadas")
resultado = map(lambda x: x + 1, map(lambda x: x * 2, numeros))
print(f"Resultado avanzado de map(): {list(resultado)}")
print('')

# Función input()
# La función input() permite al usuario ingresar datos desde la consola.
# Nota: Al ejecutar este código, Python pedirá una entrada de usuario.

# print("Ejemplo 3: Uso de input() para recibir una entrada del usuario")
# nombre = input("Introduce tu nombre: ")
# print(f"Hola, {nombre}")
# print('')

# Función len()
# La función len() devuelve la longitud (número de elementos) de un objeto iterable.

print("Ejemplo 4: Uso de len() para obtener la longitud de una lista")
lista = [10, 20, 30, 40, 50]
print(f"Longitud de la lista: {len(lista)}")
print('')

# Función sum()
# La función sum() suma todos los elementos de un iterable numérico.

print("Ejemplo 5: Uso de sum() para sumar los elementos de una lista")
numeros = [1, 2, 3, 4, 5]
print(f"Suma de los elementos de la lista: {sum(numeros)}")
print('')

# Ejemplo avanzado: Uso de sum() con un acumulador
print("Ejemplo avanzado: Uso de sum() con un acumulador")
resultado = sum(range(1, 11))  # Suma del 1 al 10
print(f"Suma de los números del 1 al 10: {resultado}")
print('')

# Función filter()
# La función filter() devuelve un iterador que contiene los elementos de un iterable que cumplen con una función dada.

print("Ejemplo 6: Uso de filter() para filtrar números pares de una lista")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = filter(lambda x: x % 2 == 0, numeros)
print(f"Números pares filtrados: {list(resultado)}")
print('')

# Ejemplo avanzado: Uso de filter() con una función personalizada
def es_impar(n):
    return n % 2 != 0

print("Ejemplo avanzado: Uso de filter() con una función personalizada")
resultado = filter(es_impar, numeros)
print(f"Números impares filtrados: {list(resultado)}")
print('')

# Función enumerate()
# La función enumerate() añade un contador a un iterable y lo devuelve en forma de un objeto enumerado.

print("Ejemplo 7: Uso de enumerate() para contar los elementos de una lista")
lenguajes = ['Python', 'Java', 'C++']
for indice, lenguaje in enumerate(lenguajes, start=1):
    print(f"{indice}. {lenguaje}")
print('')

# Ejemplo avanzado: Uso de enumerate() en conjunto con list comprehension
print("Ejemplo avanzado: Uso de enumerate() con list comprehension")
numeros = [10, 20, 30, 40]
resultado = [f"{indice}: {numero}" for indice, numero in enumerate(numeros, start=1)]
print(f"Resultado avanzado de enumerate(): {resultado}")
print('')

# Funciones adicionales importantes en Python

# Función all()
# Devuelve True si todos los elementos de un iterable son verdaderos (o si el iterable está vacío).

print("Ejemplo 8: Uso de all() para verificar si todos los elementos son verdaderos")
valores = [True, True, False]
resultado = all(valores)
print(f"Resultado de all(): {resultado}")
print('')

# Ejemplo avanzado: Uso de all() con una lista de condiciones
print("Ejemplo avanzado: Uso de all() con condiciones")
numeros = [10, 20, 30, 40]
resultado = all(x > 0 for x in numeros)  # Verifica si todos los números son mayores que 0
print(f"Todos los números son mayores que 0: {resultado}")
print('')

# Función any()
# Devuelve True si al menos un elemento de un iterable es verdadero.

print("Ejemplo 9: Uso de any() para verificar si algún elemento es verdadero")
valores = [False, False, True]
resultado = any(valores)
print(f"Resultado de any(): {resultado}")
print('')

# Ejemplo avanzado: Uso de any() con condiciones
print("Ejemplo avanzado: Uso de any() para verificar condiciones")
resultado = any(x % 2 == 0 for x in [1, 3, 5, 8])  # Verifica si al menos un número es par
print(f"Hay algún número par: {resultado}")
print('')

# Función sorted()
# Ordena los elementos de un iterable y devuelve una nueva lista ordenada.

print("Ejemplo 10: Uso de sorted() para ordenar una lista de números")
numeros = [3, 1, 4, 1, 5, 9, 2]
print(f"Lista ordenada: {sorted(numeros)}")
print('')

# Ejemplo avanzado: Uso de sorted() con claves personalizadas
print("Ejemplo avanzado: Uso de sorted() con una clave personalizada")
palabras = ['manzana', 'pera', 'uva', 'banana']
resultado = sorted(palabras, key=len)  # Ordena las palabras por longitud
print(f"Palabras ordenadas por longitud: {resultado}")
print('')

# Funciones min() y max()
# Devuelven el valor mínimo y máximo de un iterable o un conjunto de argumentos.

print("Ejemplo 11: Uso de min() y max() para encontrar valores mínimos y máximos")
numeros = [10, 20, 5, 40, 50]
print(f"Valor mínimo: {min(numeros)}")
print(f"Valor máximo: {max(numeros)}")
print('')

# Ejemplo avanzado: Uso de min() y max() con tuplas y listas de tuplas
print("Ejemplo avanzado: Uso de min() y max() con una lista de tuplas")
tuplas = [(1, 'a'), (2, 'b'), (3, 'c'), (0, 'd')]
print(f"Tupla con el valor mínimo: {min(tuplas)}")
print(f"Tupla con el valor máximo: {max(tuplas)}")
print('')

# Función abs()
# Devuelve el valor absoluto de un número.

print("Ejemplo 12: Uso de abs() para obtener el valor absoluto de un número")
numero = -15
print(f"Valor absoluto de {numero}: {abs(numero)}")
print('')

# Ejemplo avanzado: Uso de abs() con números complejos
print("Ejemplo avanzado: Uso de abs() con números complejos")
numero_complejo = 3 + 4j
print(f"Valor absoluto de {numero_complejo}: {abs(numero_complejo)}")
print('')

# Función round()
# Redondea un número a un número específico de decimales.

print("Ejemplo 13: Uso de round() para redondear un número")
numero = 3.14159
print(f"Redondeo de {numero} a 2 decimales: {round(numero, 2)}")
print('')

# Ejemplo avanzado: Uso de round() en cálculos matemáticos
print("Ejemplo avanzado: Uso de round() en cálculos matemáticos")
numero = 5.6789
redondeado = round(numero)
print(f"Redondeo de {numero}: {redondeado}")
print('')

# Funciones chr() y ord()
# chr() convierte un entero en su carácter correspondiente, y ord() convierte un carácter en su valor Unicode.

print("Ejemplo 14: Uso de chr() para convertir un entero en un carácter")
entero = 65
print(f"El carácter correspondiente a {entero} es: {chr(entero)}")
print('')

# Ejemplo avanzado: Uso de ord() para convertir un carácter en su valor Unicode
print("Ejemplo avanzado: Uso de ord() para obtener el código Unicode de un carácter")
caracter = 'A'
print(f"El código Unicode de '{caracter}' es: {ord(caracter)}")
print('')
