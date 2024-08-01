# Tema 4: Bucles en Python

# Los bucles son herramientas para alterar el flujo normal de un programa. Permiten repetir una porción de código 
# tantas veces como sea necesario con el fin de lograr un objetivo o cumplir una condición específica. 
# Python incluye únicamente dos tipos de bucle: while y for. 

# ----------------------------------------------------------------------------------------------------------------------------------------
# Bucle WHILE
# El bucle while en Python se usa para ejecutar un bloque de código repetidamente siempre que se cumpla una condición.
# La condición se evalúa antes de la ejecución del bloque de código. Si la condición es verdadera, el bloque de código se ejecuta.
# Esto continúa hasta que la condición se evalúa como falsa.

print("\nBUCLE WHILE\n")

# El bucle while requiere que las variables relevantes estén definidas anteriormente. 
# En este ejemplo es necesario definir una variable de indexación, i, inicializada en 1.
# Es importante mencionar que la variable de indexación i se debe incrementar, de lo contrario el ciclo continuará indefinidamente.
print("El código dentro del bucle while se ejecuta mientras se cumpla una condición específica")
i = 1
while i < 6:
  print("Se ejecuta el código hasta que se cumpla que i < 6")
  print(f"i = {i}")
  i += 1
print("i > 6, por lo tanto, la condición deja de cumplirse y el bucle se detiene")
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# Bucle FOR
# El bucle for en Python se usa para iterar sobre una secuencia (puede ser una lista, una tupla, un diccionario, un conjunto o una cadena).
# Es diferente a la palabra clave "for" de otros lenguajes de programación ya que funciona como un método iterador. Con el bucle for es posible 
# ejecutar un conjunto de declaraciones, una vez para cada elemento de una lista, tupla, conjunto, etc.
# A diferencia del bucle while, el bucle for en Python no requiere una variable de conteo para controlar la iteración.

print("\nBUCLE FOR\n")

print("El código dentro del bucle for se ejecuta una vez para cada elemento de un objeto iterador")
fruits = ["apple", "banana", "cherry"]
print(f'Ejemplo: ejecutando un bloque de código una vez para cada elemento de la lista: {fruits}')
for fruit in fruits:
    print("Elemento dentro de la lista:", fruit)
print('')

# Para ejecutar un bloque de código un determinado número de veces utilizando el bucle for como se utiliza en otros lenguajes de programación,
# se debe combinar con la función range(). La función range() devuelve una secuencia de números, que comienza en 0 de forma predeterminada, 
# se incrementa en 1 (de forma predeterminada) y termina en un número específico.

print("Para ejecutar un bloque de código un número específico de veces utilizando el bucle for se debe combinar con la función range()")
print("Ejemplo: ejecutando un bloque de código 6 veces")
# Se debe tener en cuenta que range(6) no incluye el valor 6, sino que genera valores del 0 al 5.
for x in range(6):
  print(f"Ejecución del código número: {x}")
print('')

# La función range() tiene por defecto 0 como valor inicial; sin embargo, es posible especificar el valor inicial agregando un parámetro: (x, y), que significa valores de x a y (sin incluir y).
# Además, la función range() por defecto incrementa la secuencia en 1, sin embargo, es posible especificar el valor del incremento agregando un tercer parámetro: range(x, y, z).
print("La función range permite especificar el valor inicial, el valor final y el valor de incremento")
print("Ejemplo: ejecutando un bloque de código desde 1 hasta 20 (sin incluir 20) con incrementos de 5")
for x in range(1, 21, 5):
  print(f"Ejecución del código número: {x}")
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# Utilizando break, continue, else y bucles anidados

# Para detener un bucle (for o while) antes de que haya recorrido todos los elementos se debe utilizar la instrucción break.
print("Utilizando la instrucción break para detener un bucle for antes de que haya finalizado el ciclo completo")
fruits = ["apple", "banana", "kiwi", "lemon", "cherry"]
print(f"Recorriendo todos los elementos de la lista {fruits} hasta que se encuentre el elemento 'lemon'")
for x in fruits:
  print("Elemento dentro de la lista:", x)
  if x == "lemon":
    break
print('')

# Para detener la iteración actual del bucle (for o while) y continuar con la siguiente se debe utilizar la instrucción continue.
print("Utilizando la instrucción continue para omitir la ejecución del código cuando se cumpla una condición específica")
fruits = ["apple", "banana", "kiwi", "lemon", "cherry"]
print(f"Recorriendo todos los elementos de la lista {fruits} exceptuando el elemento 'lemon'")
for x in fruits:
  if x == "lemon":
    continue
  print("Elemento dentro de la lista:", x)
print('')

# La palabra clave else en un bucle (for o while) especifica un bloque de código que se ejecutará cuando finalice el bucle:
# sin embargo, el bloque "else" NO se ejecutará si el bucle se detiene mediante una instrucción break.
print("Utilizando la instrucción else para ejecutar un bloque de código cuando se haya finalizado el bucle")
print("Ejemplo: ejecutando un bloque de código cuando se haya recorrido otro bloque de código 6 veces")
for x in range(6):
  print(f"Ejecución del código número: {x}")
else:
  print("El bucle ha finalizado")
  print('Se ejecuta el código dentro del bloque "else"')
print('')

# Un bucle anidado es un bucle dentro de otro bucle. El "bucle interno" se ejecutará una vez por cada iteración del "bucle externo".
# Esto significa que si el bucle externo se repite 'n' veces y el bucle interno se repite 'm' veces, el bloque de código interno se ejecutará un total de n * m veces.
print("Un bucle anidado es un bucle dentro de otro. El bucle interno se ejecuta una vez por cada iteración del bucle externo")
adjs = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
print(f"Ejemplo: utilizando un bucle anidado para recorrer la lista {adjs} a partir de los elementos de otra {fruits}")
for fruit in fruits:
  for adj in adjs:
    print(f"{fruit}: {adj}")
print('')

# Los bucles no pueden estar vacíos, pero si por alguna razón es necesario un bucle for sin contenido, se debe utilizar la palabra clave pass.
print("Los bucles no pueden estar vacíos")
for x in [0, 1, 2]:
  pass
