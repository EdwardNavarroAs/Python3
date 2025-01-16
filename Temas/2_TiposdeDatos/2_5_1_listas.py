# Tema 2: Tipos de datos en python
# 2.5.1 Listas

# Las listas se utilizan para almacenar varios elementos en una sola variable.
# Los elementos de una lista están ordenados, son modificables y permiten valores duplicados:
#   --> Los elementos tienen un orden definido y ese orden no cambiará. 
#   --> Si se agregan nuevos elementos, los nuevos elementos se colocan al final de la lista.
#   --> Es posible cambiar, agregar y eliminar elementos en una lista después de haberla creado.
#   --> Los elementos están indexados, el primer elemento tiene el índice [0], el segundo índice [1], etc
#   --> Dado que las listas están indexadas, las listas pueden tener elementos con el mismo valor (duplicados).

# ----------------------------------------------------------------------------------------------------------------------------------------
# DEFINIENDO UNA LISTA EN PYTHON
print("\nDEFINIENDO LISTAS\n")

# Las listas se definen utilizando corchetes []
print("Las listas en Python se definen utilizando corchetes []:")
my_list1 = ["apple", "banana", "cherry"]
print(f"Lista en Python: {my_list1}, Tipo de dato {type(my_list1)}")
print('')

# También se puede definir una lista utilizando el constructor list().
print("También se puede definir una lista utilizando el constructor list():")
thislist = list(("apple", "banana", "cherry")) 
print(f"Lista en Python: {thislist}, Tipo de dato: {type(thislist)}")
print('')

# Las listas pueden contener cualquier tipo de dato, incluso otras listas
print("Las listas pueden contener cualquier tipo de dato:")
list1 = [True, "apple", 5, "banana", 7, "cherry", 3, False, [1,2,3]]
print(f"Lista con diferentes tipos de datos: {list1}")
print('')

# Las listas permiten elementos duplicados
print("Las listas permiten elementos duplicados:")
my_list2 = ["apple", "banana", 5, "cherry", "apple", "cherry", 5]
print(f"Lista con elementos duplicados: {my_list2}")
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# ACCEDIENDO A ELEMENTOS ESPECIFICOS DE UNA LISTA
print("\nACCEDIENDO A ELEMENTOS ESPECIFICOS DE UNA LISTA\n")

# Para determinar si un elemento específico está presente en una lista, se utiliza la palabra clave in.
print("Verificando si un elemento específico se encuentra en una lista:")
my_list3 = ["apple", "banana", "cherry"]
result = 'apple' in my_list3
print(f"Verificando si 'apple' se encuentra presente en la lista {my_list3}, resultado: {result}")
print('')

# Los elementos de la lista están indexados, por lo tanto, pueden ser accedidos consultando el número de índice correspondiente.
print('Accediendo a elementos específicos de una lista:')
list2 = ["apple", "banana", "cherry"]   # el primer elemento tiene el índice [0], el segundo índice [1], etc.
print(f"Accediendo al segundo elemento de la lista {list2}: {list2[1]}")
print('')

# Python permite la indexación negativa, lo que significa comenzar desde el final. -1 se refiere al último elemento, -2 se refiere al penúltimo elemento, etc.
print('Indexación negativa de listas en Python:')
print(f"Accediendo al último elemento de la lista {list2}: {list2[-1]}")
print('')

# Las listas permiten especificar un rango de índices, indicando el inicio y el final.
# Al especificar un rango, el valor que se retorna es una nueva lista con los elementos especificados.
print("Las listas permiten especificar un rango de índices:")
list3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(f"Accediendo desde el tercer hasta el quinto elemento de la lista {list3}: {list3[2:5]}") # La búsqueda comienza en el índice 2 (incluido) y finaliza en el índice 5 (no incluido).
print('')

# Al omitir el valor inicial, el rango comenzará en el primer elemento.
print("Si no se especifica el índice inicial, el rango comenzará en el primer elemento:")
print(f"Accediendo desde el primer hasta el cuarto elemento de la lista {list3}: {list3[:4]}") # La búsqueda comienza desde el primer elemento (incluido) y finaliza en el índice 4 (no incluido).
print('')

# Al omitir el valor final, el rango continuará hasta el final de la lista.
print("Si no se especifica el índice final, el rango comenzará desde el elemento especificado hasta el final:")
print(f"Accediendo desde el tercer hasta el último elemento de la lista {list3}: {list3[2:]}") # La búsqueda comienza desde el tercer elemento (incluido) y continúa hasta el final de la lista.
print('')

# Al especificar índices negativos, la búsqueda se inicia desde el final de la lista.
print("Si se especifican índices negativos, la búsqueda se inicia desde el final:")
print(f"Accediendo desde el segundo hasta el penúltimo elemento de la lista {list3}: {list3[-6:-1]}") # La búsqueda comienza en el índice -6 (incluido) y finaliza en el índice -2 (no incluido).
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CAMBIANDO ELEMENTOS DE UNA LISTA
print("\nCAMBIANDO ELEMENTOS DE UNA LISTA\n")

# para cambiar el valor de un elemento especifico, se debe consultar el número del indice
print("Para cambiar el valor de un elemento en una lista, se debe consultar el número del indice")
thislist = ["apple", "banana", "cherry"]
print(f"cambiando el segundo elemento de la lista: {thislist}")
thislist[1] = "mango"
print(f"lista modificada: {thislist}")
print('')

# Para cambiar el valor de los elementos dentro de un rango específico, se debe definir una lista con los nuevos valores y consultar el rango de números de índice donde se desea insertar los nuevos valores.
print("Para cambiar varios elementos de una lista, se debe consultar el rango específico que se desea cambiar y asignarle los nuevos valores mediante otra lista")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(f"Cambiando el segundo y tercer elemento de la lista: {thislist}")
thislist[1:3] = ["blackcurrant", "watermelon"]
print(f"Lista modificada: {thislist}")
print('')

# Si se insertan más elementos de los que se desean reemplazar, los nuevos elementos se insertarán donde se especificó y los elementos restantes se moverán en consecuencia
# Sin embargo, la longitud de la lista cambiará cuando la cantidad de elementos insertados no coincida con la cantidad de elementos reemplazados.
print("Si se insertan más elementos de los que se reemplazan, los nuevos elementos se insertan donde se especificó y los elementos restantes se mueven en consecuencia")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(f"Cambiando el segundo y tercer elemento de la lista: {thislist}")
thislist[1:3] = ["blackcurrant", "watermelon", "lemon"]
print(f"Lista modificada: {thislist}")
print('')

# Si se insertan menos elementos de los que se desean reemplazar, los nuevos elementos se insertarán donde se especificó y los elementos restantes se moverán en consecuencia:
print("Si se insertan menos elementos de los que se reemplazan, los nuevos elementos se insertan donde se especificó y los elementos restantes se mueven en consecuencia")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(f"Cambiando el segundo y tercer elemento de la lista: {thislist}")
thislist[1:3] = ["lemon"]
print(f"Lista modificada: {thislist}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# AGREGANDO ELEMENTOS A UNA LISTA
print("\nAGREGANDO ELEMENTOS A UNA LISTA\n")

# El método append() se utiliza para agregar un elemento al final de una lista:
print("El método append() se utiliza para agregar nuevos elementos al final de una lista.")
thislist = ["apple", "banana", "cherry"]
print(f"Agregando el elemento 'orange' a la lista: {thislist}")
thislist.append("orange")
print(f"Lista modificada: {thislist}")
print('')

# El método insert() se utiliza para insertar un nuevo elemento de la lista en una posición específica, sin reemplazar ninguno de los valores existentes:
print("El método insert() se utiliza para agregar un nuevo elemento a una lista en una posición específica.")
mylist = ["apple", "banana", "cherry"]
print(f"Agregando el elemento 'watermelon' en la tercera posicion de la lista: {mylist}")
mylist.insert(2, "watermelon")
print(f"Lista modificada: {mylist}")
print('')

# El método extend() se utiliza para agregar elementos de otra lista a la lista actual.
print("El método extend() se utiliza para agregar elementos de una lista a otra")
aux_list= ["mango", "lemon"]
print(f"Agregando los elementos de {aux_list} a la lista: {thislist}")
thislist.extend(aux_list)
print(f"Lista modificada: {thislist}")
print('')

# El método extend() no solo agrega listas, también puede agregar cualquier objeto iterable (tuplas, conjuntos, diccionarios, etc.).
print("El método extend() permite agregar cualquier objeto iterable.")
aux_iter = ('lemon', 'mango')
thislist = ["apple", "banana", "cherry"]
print(f"Agregando el iterable {aux_iter} a la lista: {thislist}")
thislist.extend(aux_iter)
print(f"Lista modificada: {thislist}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ELIMINANDO ELEMENTOS DE UNA LISTA
print("\nELIMINANDO ELEMENTOS DE UNA LISTA\n")

# El método remove() se utiliza para eliminar un elemento específico de una lista.
print("El método remove() se utiliza para eliminar elementos de una lista.")
thislist = ["apple", "banana", "cherry"]
print(f"Eliminando el elemento 'banana' de la lista: {thislist}")
thislist.remove("banana")
print(f"Lista modificada: {thislist}")
print('')

# Si hay más de un elemento con el valor especificado, el método remove() elimina el primero de ellos.
# Este metodo elimina el primer elemento con el valor especificado y genera un error si el elemento no está presente en la lista.
print("Si hay más de un elemento con el valor especificado, el método remove() elimina el primero de ellos.")
thislist = ["apple", "banana", "lemon", "cherry", "banana"]
print(f"Eliminando el primer elemento 'banana' de la lista: {thislist}")
thislist.remove("banana")
print(f"Lista modificada: {thislist}")
print('')

# El método pop() se utiliza para eliminar un elemento en una posición específica de una lista.
print("El método pop() se utiliza para eliminar un elemento en una posición específica de una lista.")
thislist = ["apple", "banana", "lemon", "cherry", "banana"]
print(f"Eliminando el tercer elemento de la lista: {thislist}")
thislist.pop(2)
print(f"Lista modificada: {thislist}")
print('')

# Si no se especifica el índice, el método pop() elimina el último elemento.
# Este metodo elimina el elemento en la posición especificada (o el último si no se proporciona un índice), y no genera ningún error si el elemento no está presente en la lista.
print("Si no se especifica la posicion el método pop() elimina el último elemento de una lista.")
thislist = ["apple", "banana", "lemon", "cherry", "banana"]
print(f"Eliminando el último elemento de la lista: {thislist}")
thislist.pop()
print(f"Lista modificada: {thislist}")
print('')

# El método clear() se utiliza para vaciar el contenido de una lista. La lista aún permanece, pero no tiene contenido.
print("El método clear() se utiliza para vaciar una lista.")
thislist = ["apple", "banana", "lemon", "cherry", "banana"]
print(f"Eliminando el contenido de la lista: {thislist}")
thislist.clear()
print(f"Lista modificada: {thislist}")
print('')

# Para eliminar un elemento en una posición específica, también se puede utilizar la palabra clave del.
print("Para eliminar un elemento específico de una lista tambien se puede utilizar la palabra clave del")
thislist = ["apple", "banana", "cherry"]
print(f"Eliminando el tercer elemento de la lista: {thislist}")
del thislist[2]
print(f"Lista modificada: {thislist}")
print('')

# Para eliminar una lista completamente, se utiliza la palabra clave del.
# Esto libera la memoria asociada con la lista, lo que puede ser útil en programas con grandes cantidades de datos
print("La palabra clave del tambien se utiliza para eliminar completamente una lista.")
print(f"Eliminando la lista: {thislist}")
del thislist
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# RECORRIENDO ELEMENTOS DE UNA LISTA
print("\nRECORRIENDO ELEMENTOS DE UNA LISTA\n")

# Para recorrer todos los elementos de una lista, se utiliza un bucle for.
print("Recorriendo los elementos de una lista utilizando un bucle for.")
my_list1 = ["apple", "mango", "lemon", "banana"]
print(f"Los elementos de la lista {my_list1} son:")
for element in my_list1:
    print(f'Elemento de la lista: {element}')
print('')

# Para recorrer los elementos de una lista consultando su número de índice, se utilizan las funciones range() y len().
# Esto es menos eficiente que usar un bucle for directamente. Debido a que implica una llamada a len() en cada iteración.
print("Recorriendo los elementos de una lista consultando su índice utilizando las funciones range() y len().")
print(f"Los elementos de la lista {my_list1} son:")
for index in range(len(my_list1)):
    print(f'Elemento de la lista: {my_list1[index]}')
print('')

# También es posible recorrer los elementos de una lista utilizando un bucle while.
print("Recorriendo los elementos de una lista utilizando un bucle while.")
print(f"Los elementos de la lista {my_list1} son:")
i = 0
while i < len(my_list1):
    print(f'Elemento de la lista: {my_list1[i]}')
    i += 1
print('')

# Python ofrece una sintaxis más corta para recorrer los elementos de una lista, denominada comprensión de listas.
print("Recorriendo los elementos de una lista utilizando la comprensión de listas.")
[print(f'Elemento de la lista: {element}') for element in my_list1]
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# COMPRENSIÓN DE LISTAS EN PYTHON
print("\nCOMPRENSIÓN DE LISTAS EN PYTHON\n")

# La comprensión de listas ofrece una sintaxis más corta cuando se desea crear una nueva lista basada en los 
# valores de una lista existente.
# Sintaxis:
# newlist = [expression for item in iterable if condition == True]
# El valor de retorno es una lista nueva, que deja la lista original sin cambios.

# Utilizando la comprensión de listas para crear nuevas listas bajo condiciones específicas.
print("Utilizando la comprensión de listas para crear una nueva lista.")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(f"Lista original: {fruits}")
fruits_with_a = [fruit for fruit in fruits if "a" in fruit]
fruits_without_kiwi = [fruit for fruit in fruits if fruit != "kiwi"]
print(f"Lista solo con elementos que contengan la letra 'a': {fruits_with_a}")
print(f"Lista excluyendo el elemento 'kiwi': {fruits_without_kiwi}")
print()

# El iterable puede ser cualquier objeto iterable, como una lista, tupla, conjunto, etc.
print("El iterable puede ser cualquier objeto iterable.")
print("Utilizando la comprensión de listas y la función range() para crear listas de números enteros.")
digit_list = [digit + 1 for digit in range(10)]
digit_list_less_than_5 = [digit + 1 for digit in range(10) if digit < 5]
print(f"Lista con números del 1 al 10: {digit_list}")
print(f"Lista con números del 1 al 5: {digit_list_less_than_5}")
print()

# En la sintaxis de comprensión de listas, la expresión es el elemento actual en la iteración, 
# que también es el resultado y puede ser manipulado antes de ser añadido a la nueva lista.
print("La expresión representa los elementos resultado que contendrá la nueva lista, los cuales pueden ser manipulados.")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_upper = [fruit.upper() for fruit in fruits]
print(f"Lista original: {fruits}")
print(f"Lista en mayúsculas: {fruits_upper}")
print()

# En la sintaxis de comprensión de listas, la expresión también puede contener condiciones, no solo como un filtro,
# sino como una forma de manipular el resultado.
print("La expresión puede contener condiciones como una forma de manipular el resultado.")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [fruit if fruit != "banana" else "lemon" for fruit in fruits]
print(f"Lista original: {fruits}")
print(f"Lista manipulada: {newlist}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ORDENANDO ELEMENTOS DE UNA LISTA
print("\nORDENANDO ELEMENTOS DE UNA LISTA\n")

# ORDENANDO ELEMENTOS DE UNA LISTA
print("\nORDENANDO ELEMENTOS DE UNA LISTA\n")

# Las listas tienen un método sort() que ordena la lista alfanuméricamente de forma ascendente de manera predeterminada.
# Nota: de forma predeterminada, el método sort() distingue entre mayúsculas y minúsculas, lo que da como resultado que todas las letras mayúsculas se ordenen antes que las minúsculas.
print("El método sort() se utiliza para ordenar los elementos de una lista de forma ascendente por defecto.")
fruits = ["orange", "mango", "kiwi", "pineapple", "Banana"]
numbers = [100, 50, 65, 82, 23]
print(f"Lista de frutas original: {fruits}")
print(f"Lista de números original: {numbers}")
fruits.sort()
numbers.sort()
print(f"Lista de frutas ordenada: {fruits}")
print(f"Lista de números ordenada: {numbers}")
print('')

# Para ordenar de forma descendente, se debe utilizar el argumento reverse = True.
print("Utilizando el método sort() para ordenar los elementos de una lista de forma descendente.")
numbers = [100, 50, 65, 82, 23]
print(f"Lista original: {numbers}")
numbers.sort(reverse=True)
print(f"Lista ordenada: {numbers}")
print('')

# También se pueden ordenar los elementos de una lista mediante una función personalizada utilizando el argumento key.
print("El argumento key se utiliza para ordenar una lista mediante una función personalizada.")
print("Ordenando una lista de menor a mayor según su proximidad a 50.")
def myfunction(n):
    return abs(n - 50)

numbers = [100, 50, 65, 82, 23]
print(f"Lista original: {numbers}")
numbers.sort(key=myfunction)
print(f"Lista ordenada: {numbers}")
print('')

# El método reverse() se utiliza para invertir el orden de clasificación actual de los elementos.
print("El método reverse() se utiliza para invertir el orden de clasificación de los elementos de una lista.")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(f"Lista original: {thislist}")
thislist.reverse()
print(f"Lista invertida: {thislist}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# COPIANDO UNA LISTA
print("\nCOPIANDO UNA LISTA\n")

# No se puede copiar una lista simplemente escribiendo lista2 = lista1, porque: 
# lista2 solo será una referencia a lista1, y los cambios realizados en lista1 también se realizarán automáticamente en lista2.

# Una de las formas correctas de realizar una copia de una lista es utilizando el método copy().
print("Utilizando el método copy() para copiar una lista.")
thislist = ["apple", "banana", "cherry"]
print(f"Lista original: {thislist}")
mylist = thislist.copy()
print(f"Lista copiada: {mylist}")
print('')

# Otra forma de hacer una copia de una lista es utilizar el método integrado list()
print("Utilizando el método list() para copiar una lista.")
thislist = ["apple", "banana", "cherry"]
print(f"Lista original: {thislist}")
mylist = list(thislist)
print(f"Lista copiada: {mylist}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# UNIENDO LISTAS
print("\nUNIENDO LISTAS\n")

# Una de las formas más sencillas para unir listas en Python es utilizando el operador +, donde se crea una lista nueva con los elementos de las listas unidas.
print("Uniendo listas utilizando el operador +")
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
print(f"Las listas que se unirán son: Lista1 = {list1}, Lista2 = {list2}")
list3 = list1 + list2
print(f"Listas unidas: {list3}")
print('')

# Otra manera de unir listas es utilizando el método extend(), donde el propósito es agregar elementos de una lista a otra:
print("Uniendo listas utilizando el método extend()")
list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]
print(f"Las listas que se unirán son: Lista1 = {list1}, Lista2 = {list2}")
list1.extend(list2)
print(f"Listas unidas: {list1}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# METODOS ADICIONALES DE LISTAS
print("\nPRINCIPALES METODOS DE LISTAS\n")

# El método len() determina cuántos elementos estan presentes una lista
print("El metodo len() determina el número de elementos dentro de una lista")
list1 = [1,2,3,4,5]
print(f"la lista {list1} tiene un total de {len(list1)} elementos")
print('')

# El método count() determina el número de veces que aparece un elemento específico en una lista:
print("El método count() determina cuántas veces un elemento aparece dentro de una lista")
list1 = ["a", "b", "c", "a", "d", "e", "a"]
x = list1.count("a")
print(f"El número de veces que aparece la letra \"a\" dentro de la lista {list1} es: {x}")
print('')

# El método index() determina la posición del primer elemento que coincide con el valor especificado dentro de una lista:
print("El método index() determina la posición del primer elemento que coincide con un valor específico dentro de una lista")
list2 = [1, 2, 3, 2, 4, 5, 6, 2]
y = list2.index(2)
print(f"El primer elemento con valor igual a 2 dentro de la lista {list2} se encuentra en la posición {y}")
print('')

# El método max() determina el elemento máximo de una lista. 
print("El método max() determina el elemento máximo de una lista")
numbers = [10, 5, 8, 20, 3]
max_number = max(numbers)
print(f"El elemento máximo de la lista {numbers} es: {max_number}")  # Salida: El elemento máximo de la lista es: 20
print('')

# El método min() determina el elemento mminimo de una lista. 
print("El método min() determina el elemento minimo de una lista")
numbers = [10, 5, 8, 20, 3]
min_number = min(numbers)
print(f"El elemento minimo de la lista {numbers} es: {min_number}") 
print('')

# El método sum() determina la suma de los elementos de una lista. 
print("El método sum() determina la suma de los elementos de una lista")
numbers = [10, 5, 8, 20, 3]
sum_numbers = sum(numbers)
print(f"La suma de los elementos de la lista {numbers} es: {sum_numbers}")
print('')

# El método any() determina True si almenos uno de los elementos de un iterable (lista entre otros) es verdadero
print("El método any() determina si almenos uno de los elementos de una lista es verdadero")
values = [False, False, True, False]
result = any(values)
print(f"¿Hay algún valor verdadero en la lista {values}?, respuesta: {result}") 
print('')

# El método all() determina True si todos los elementos de un iterable (lista entre otros) son verdaderos
print("El método all() determina si todos los elementos de una lista son verdaderos")
values = [True, False, True, False]
result = all(values)
print(f"¿Todos los elementos de la lista {values} son verdaderos?, respuesta: {result}") 
print('')
