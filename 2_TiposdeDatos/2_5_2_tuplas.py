# Tema 2: Tipos de datos en python
# 2.5.2 tuplas

# Las tuplas se utilizan para almacenar varios elementos en una sola variable.
# Los elementos de una tupla están ordenados, no se pueden modificar (inmutables) y permiten valores duplicados.
#   --> Los elementos tienen un orden definido y ese orden no cambiará.
#   --> Las tuplas no se pueden modificar, lo que significa que no es posible cambiar, agregar o eliminar elementos una vez creada la tupla.
#   --> Los elementos están indexados, el primer elemento tiene el índice [0], el segundo índice [1], etc
#   --> Dado que las tuplas están indexadas, las tuplas pueden tener elementos con el mismo valor (duplicados).

# ----------------------------------------------------------------------------------------------------------------------------------------
# DEFINIENDO UNA TUPLA EN PYTHON
print("\nDEFINIENDO TUPLAS\n")

# Las tuplas se definen utilizando paréntesis ()
print("Las tuplas en Python se definen utilizando corchetes ():")
my_tuple = ("apple", "banana", "cherry")
print(f"Tupla en Python: {my_tuple}, Tipo de dato: {type(my_tuple)}")
print('')

# También se puede definir una tupla utilizando el constructor list()
print("También se puede definir una tupla utilizando el constructor tuple():")
thistuple = tuple(["apple", "banana", "cherry"]) 
print(f"Tupla en Python: {thistuple}, Tipo de dato: {type(thistuple)}")
print('')

# Las tuplas pueden contener cualquier tipo de dato, incluso otras tuplas
print("Las tuplas pueden contener cualquier tipo de dato:")
tuple1 = (True, "apple", 5, "banana", 7, "cherry", 3, False, [1,2,3], (4,5,6))
print(f"Tupla con diferentes tipos de datos: {tuple1}")
print('')

# Las tuplas permiten elementos duplicados
print("Las tuplas permiten elementos duplicados:")
my_tuple = ("apple", "banana", 5, "cherry", "apple", "cherry", 5)
print(f"Tupla con elementos duplicados: {my_tuple}")
print('')

# Para crear una tupla con un solo elemento, se debe agregar una coma después del elemento; de lo contrario, 
# Python no lo reconocerá como una tupla.
print("Para crear una tupla con un solo elemento, se debe agregar una coma después del elemento; de lo contrario, Python no lo reconocerá como una tupla")
thistuple = ("apple",)
thisnotatuple = ("apple")
print(f"Tupla de un solo elemento: {thistuple}, Tipo de dato: {type(thistuple)}")
print(f"Elemento dentro de un par de paréntesis (no es una tupla si no se agrega la coma al final): {thisnotatuple}, Tipo de dato: {type(thisnotatuple)}")
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# ACCEDIENDO A ELEMENTOS DE UNA TUPLA
print("\nACCEDIENDO A ELEMENTOS DE UNA TUPLA\n")

# Para determinar si un elemento específico está presente en una tupla, se utiliza la palabra clave in.
print("Verificando si un elemento específico se encuentra en una tupla:")
my_tuple = ("apple", "banana", "cherry")
result = 'apple' in my_tuple
print(f"Verificando si 'apple' se encuentra presente en la tupla {my_tuple}, resultado: {result}")
print('')

# Los elementos de la tupla están indexados, por lo tanto, pueden ser accedidos consultando el número de índice correspondiente.
print('Accediendo a elementos específicos de una tupla:')
tuple2 = ("apple", "banana", "cherry")   # el primer elemento tiene el índice [0], el segundo índice [1], etc.
print(f"Accediendo al segundo elemento de la tupla {tuple2}: {tuple2[1]}")
print('')

# Python permite la indexación negativa, lo que significa comenzar desde el final. -1 se refiere al último elemento, -2 se refiere al penúltimo elemento, etc.
print('Indexación negativa de tuplas en Python:')
print(f"Accediendo al último elemento de la tupla {tuple2}: {tuple2[-1]}")
print('')

# Las tuplas permiten especificar un rango de índices, indicando el inicio y el final.
# Al especificar un rango, el valor que se retorna es una nueva tupla con los elementos especificados.
print("Las tuplas permiten especificar un rango de índices:")
tuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(f"Accediendo desde el tercer hasta el quinto elemento de la tupla {tuple3}: {tuple3[2:5]}") # La búsqueda comienza en el índice 2 (incluido) y finaliza en el índice 5 (no incluido).
print('')

# Al omitir el valor inicial, el rango comenzará en el primer elemento.
print("Si no se especifica el índice inicial, el rango comenzará en el primer elemento:")
print(f"Accediendo desde el primer hasta el cuarto elemento de la tupla {tuple3}: {tuple3[:4]}") # La búsqueda comienza desde el primer elemento (incluido) y finaliza en el índice 4 (no incluido).
print('')

# Al omitir el valor final, el rango continuará hasta el final de la tupla.
print("Si no se especifica el índice final, el rango comenzará desde el elemento especificado hasta el final:")
print(f"Accediendo desde el tercer hasta el último elemento de la tupla {tuple3}: {tuple3[2:]}") # La búsqueda comienza desde el tercer elemento (incluido) y continúa hasta el final de la tupla.
print('')

# Al especificar índices negativos, la búsqueda se inicia desde el final de la tupla.
print("Si se especifican índices negativos, la búsqueda se inicia desde el final:")
print(f"Accediendo desde el segundo hasta el penúltimo elemento de la tupla {tuple3}: {tuple3[-6:-1]}") # La búsqueda comienza en el índice -6 (incluido) y finaliza en el índice -2 (no incluido).
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MODIFICANDO LOS ELEMENTOS DE TUPLAS
print("\nMODIFICANDO LOS ELEMENTOS DE TUPLAS\n")

# Las tuplas no se pueden modificar, lo que significa que no se pueden cambiar, agregar ni eliminar elementos una vez creada la tupla.
# sin embargo, existen algunas alternativas para realizar este procedimiento en caso de ser necesario
# Es posible convertir la tupla en una lista, cambiar los elementos de la lista y luego convertir la lista nuevamente en una tupla
print("Para modificar una tupla se debe convertir la tupla en una lista, modificarla y luego convertirla nuevamente en tupla")
my_tuple = ("apple", "banana", "cherry")
my_list = list(my_tuple)
print(f"Tupla original: {my_tuple}")
print(f"Tupla convertida en lista: {my_list}")
my_list[1] = "kiwi"
print(f"se modifica el segundo elemento de la lista: {my_list}")
my_new_tuple = tuple(my_list)
print(f"se convierte nuevamente la lista a una tupla: {my_new_tuple}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# AGREGANDO ELEMENTOS A UNA TUPLA
print("\nAGREGANDO ELEMENTOS A UNA TUPLA\n")

# Dado que las tuplas son inmutables, no tienen un método append() incorporado para agregar elementos, pero existen otras formas de lograrlo de ser necesario:
# Es posible convertir la tupla en una lista, agregar elementos y convertirla nuevamente en una tupla.
print("Para agregar elementos a una tupla se debe convertir la tupla en una lista, modificarla y luego convertirla nuevamente en tupla")
my_tuple = ("apple", "banana", "cherry")
my_list = list(my_tuple)
print(f"Tupla original: {my_tuple}")
print(f"Tupla convertida en lista: {my_list}")
my_list.append("kiwi") 
print(f"se agrega el elemento 'kiwi' a la lista: {my_list}")
my_new_tuple = tuple(my_list)
print(f"se convierte nuevamente la lista a una tupla: {my_new_tuple}")
print('')

# Python permite agregar tuplas a otras tuplas. Para agregar elementos a una tupla existente, estos elementos deben estar dentro de otra tupla.
print("Python permite agregar tuplas a otras tuplas. Para agregar elementos a una tupla existente, estos elementos deben estar dentro de otra tupla.")
thistuple = ("apple", "banana", "cherry")
elements = ("orange",)
print(f"Tupla original: {thistuple}")
print(f"Elementos a agregar: {elements}")
new_tuple = thistuple + elements
print(f"Tupla resultante: {new_tuple}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ELIMINANDO ELEMENTOS DE UNA TUPLA
print("\nELIMINANDO ELEMENTOS DE UNA TUPLA\n")

# Las tuplas no se pueden cambiar, por lo que no es posible eliminar elementos, pero existen otras formas de lograrlo de ser necesario:
# Es posible convertir la tupla en una lista, eliminar elementos y convertirla nuevamente en una tupla
print("Para eliminar elementos dentro de una tupla se debe convertir la tupla en una lista, modificarla y luego convertirla nuevamente en tupla")
my_tuple = ("apple", "banana", "cherry")
my_list = list(my_tuple)
print(f"Tupla original: {my_tuple}")
print(f"Tupla convertida en lista: {my_list}")
my_list.remove("banana") 
print(f"se elimina el segundo elemento de la lista: {my_list}")
my_new_tuple = tuple(my_list)
print(f"se convierte nuevamente la lista a una tupla: {my_new_tuple}")
print('')

# Para eliminar una tupla completamente, se utiliza la palabra clave del.
# Esto libera la memoria asociada con la tupla, lo que puede ser útil en programas con grandes cantidades de datos
print("La palabra clave del se utiliza para eliminar completamente una tupla")
print(f"Eliminando la tupla: {my_tuple}")
del my_tuple
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DESEMPAQUETANDO UNA TUPLA
print("\nDESEMPAQUETANDO UNA TUPLA\n")
# en Python, es posible extraer los valores de una tupla en variables. Esto es conocido como "desempaquetar una tupla":
# Nota: El desempaquetamiento de valores también se puede aplicar a las listas en Python. Funciona de la misma manera que con las tuplas.
# Sin embargo, se utilizan mas conmunmente tuplas para este proceso debido a que las tuplas son inmutables, lo que significa que sus valores no pueden modificarse después de su creación. Esto proporciona cierta seguridad y garantiza que los valores desempaquetados no cambien accidentalmente durante la ejecución del programa.
# Ademas, en terminos de rendimiento las tuplas son generalmente más eficientes que las listas, ya que su estructura inmutable permite que el intérprete de Python realice ciertas optimizaciones.

# desempaquentando una tupla en python
print("es posible extraer los valores de una tupla en variables, lo que se conoce como desempaquetamiento de tuplas")
fruits = ("apple", "banana", "cherry")
(x, y, z) = fruits
print(f"los elementos extraidos de la tupla {fruits} son: {x}, {y}, {z}")
print('')

# La cantidad de variables debe coincidir con la cantidad de valores en la tupla; de lo contrario, se debe usar un asterisco para recopilar los valores restantes como una lista.
# Si el número de variables es menor que el número de elementos dentro de la tupla, se debe agregar un * al nombre de la variable para que los elementos restantes se asignen a la variable como una lista:
print("si el numero de variables es menor que el numero de elementos dentro de la tupla, se debe utilizar un * para que los elementos restantes se asignen a la variable como una lista")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(x, y, *z) = fruits
print(f"los elementos extraidos de la tupla {fruits} son: {x}, {y}, {z}")
print('')

# Si el asterisco se agrega a otro nombre de variable distinto del último, Python asignará los elementos de la tupla a la variable hasta que el número de elementos restantes coincida con el número de variables restantes:
print("Si el asterisco se agrega a otro nombre de variable distinto del último, Python asignará los elementos de la tupla a la variable hasta que el número de elementos restantes coincida con el número de variables restantes")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(x, *y, z) = fruits
print(f"los elementos extraidos de la tupla {fruits} son: {x}, {y}, {z}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# RECORRIENDO ELEMENTOS DE UNA LISTA
print("\nRECORRIENDO ELEMENTOS DE UNA LISTA\n")

# Para recorrer todos los elementos de una tupla, se utiliza un bucle for.
print("Recorriendo los elementos de una tupla utilizando un bucle for.")
my_tuple = ("apple", "mango", "lemon", "banana")
print(f"Los elementos de la tupla {my_tuple} son:")
for element in my_tuple:
    print(f'Elemento de la tupla: {element}')
print('')

# Para recorrer los elementos de una tupla consultando su número de índice, se utilizan las funciones range() y len().
# Esto es menos eficiente que usar un bucle for directamente. Debido a que implica una llamada a len() en cada iteración.
print("Recorriendo los elementos de una tupla consultando su índice utilizando las funciones range() y len().")
print(f"Los elementos de la tupla {my_tuple} son:")
for index in range(len(my_tuple)):
    print(f'Elemento de la tupla: {my_tuple[index]}')
print('')

# También es posible recorrer los elementos de una tupla utilizando un bucle while.
print("Recorriendo los elementos de una tupla utilizando un bucle while.")
print(f"Los elementos de la tupla {my_tuple} son:")
i = 0
while i < len(my_tuple):
    print(f'Elemento de la tupla: {my_tuple[i]}')
    i += 1
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# COPIANDO UNA TUPLA
print("\nCOPIANDO UNA TUPLA\n")
# las tuplas no tienen un método copy() como las listas en Python. Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación. 
# Por lo tanto, no necesitan un método copy() para crear copias, ya que no se pueden modificar de ninguna manera
# Sin embargo,  Si se necesita una copia de una tupla independiente, se puede lograr utilizando la operación de rebanado completa ([:]) o el metodo integrado tuple():
print("A pesar de ser inmutables, es posible crear copias de una tupla utilizando la operación de rebanado completa ([:]) o el metodo integrado tuple()")
original_tuple = (1, 2, 3)
copied_tuple1 = original_tuple[:]
copied_tuple2 = tuple(original_tuple)
print(f"Tupla original: {original_tuple}")
print(f"Copia de la tupla utilizando rebanado completo [:]: {copied_tuple1}")
print(f"copia de la tupla utilizando el metodo tuple(): {copied_tuple2}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# UNIENDO TUPLAS
print("\nUNIENDO TUPLAS\n")

# Una de las formas más sencillas para unir tuplas en Python es utilizando el operador +, donde se crea una lista nueva con los elementos de las tuplas unidas.
print("Uniendo tuplas utilizando el operador +")
tuple1 = [1, 2, 3, 4]
tuple2 = [5, 6, 7, 8]
print(f"Las tuplas que se unirán son: Tupla1 = {tuple1}, Tupla2 = {tuple2}")
tuple3 = tuple1 + tuple2
print(f"tuplas unidas: {tuple3}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MULTIPLICANDO TUPLAS
print("\nMULTIPLICANDO TUPLAS\n")

# Es posible multiplicar el contenido de una tupla un número determinado de veces, utilizando el operador *
print("Para multiplicar el contenido de una tupla se debe utilizar el operador *")
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(f"Tupla original: {fruits}")
print(f"Tupla multiplicada 2 veces: {mytuple}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# METODOS ADICIONALES DE TUPLAS
print("\nPRINCIPALES METODOS DE TUPLAS\n")

# El método len() determina cuántos elementos estan presentes en una tupla
print("El metodo len() determina el número de elementos dentro de una tupla")
tuple1 = [1,2,3,4,5]
print(f"la tupla {tuple1} tiene un total de {len(tuple1)} elementos")
print('')

# El método count() determina el número de veces que aparece un elemento específico en una tupla:
print("El método count() determina cuántas veces un elemento aparece dentro de una tupla")
tuple1 = ("a", "b", "c", "a", "d", "e", "a")
x = tuple1.count("a")
print(f"El número de veces que aparece la letra \"a\" dentro de la tupla {tuple1} es: {x}")
print('')

# El método index() determina la posición del primer elemento que coincide con el valor especificado dentro de una tupla:
print("El método index() determina la posición del primer elemento que coincide con un valor específico dentro de una tupla")
tuple2 = (1, 2, 3, 2, 4, 5, 6, 2)
y = tuple2.index(2)
print(f"El primer elemento con valor igual a 2 dentro de la tupla {tuple2} se encuentra en la posición {y}")
print('')
