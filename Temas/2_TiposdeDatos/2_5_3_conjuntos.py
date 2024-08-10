# Tema 2: Tipos de datos en python
# 2.5.3 conjuntos

# Los conjuntos se utilizan para almacenar varios elementos en una sola variable.
# Los elementos de un conjunto no están ordenados (los conjuntos son no indexados), no se pueden modificar (inmutables) y no pero permiten valores duplicados.
#   --> Los elementos de un conjunto no están ordenados, no se pueden cambiar y no permiten valores duplicados. 
#   --> Una vez que se crea un conjunto, no es posible cambiar sus elementos, pero si es posible eliminar elementos y agregar elementos nuevos.
#   --> Los elementos de un conjuntos pueden aparecer en un orden diferente cada vez que se usa el conjunto y no se puede hacer referencia a ellos mediante índice o clave.

# ----------------------------------------------------------------------------------------------------------------------------------------
# DEFINIENDO UN CONJUNTO  EN PYTHON
print("\nDEFINIENDO CONJUNTOS\n")

# Los conjuntos se definen utilizando llaves {}
print("los conjuntos en en Python se definen utilizando llaves {}:")
my_set = {"apple", "banana", "cherry"}
print(f"Conjunto en Python: {my_set}, Tipo de dato: {type(my_set)}")
print('')

# También se puede definir un conjunto utilizando el constructor set()
print("También se puede definir un conjunto utilizando el constructor set():")
thisset = set(("apple", "banana", "cherry")) 
print(f"Conjunto en Python: {thisset}, Tipo de dato: {type(thisset)}")
print('')

# Los conjuntos pueden contener cualquier tipo de dato, excepto elementos mutables, como listas o conjuntos (sin embargo, un conjunto sí puede contener tuplas, por ejemplo)
print("Los conjuntos pueden contener cualquier tipo de dato no mutable:")
set1 = {True, "apple", 5, "banana", 7, "cherry", 3, False, (1,2,3)}
print(f"Conjunto con diferentes tipos de datos: {set1}")
print('')

# Los conjuntos no pueden tener elementos duplicados. Por lo tanto los valores duplicados seran ignorados
print("Los conjuntos no permiten elementos duplicados, los valores duplicados son ignorados")
my_tuple = ("apple", "banana", 5, "cherry", "apple", "cherry", 5)
my_set = {"apple", "banana", 5, "cherry", "apple", "cherry", 5}
print(f"intentado agregar elementos duplicados a un conjunto: {my_tuple}")
print(f"Conjunto resultante: {my_set}")
print('')

# Los valores True y 1 se consideran el mismo valor en conjuntos, por lo tanto, son tratados como duplicados:
print("Los valores True y 1 se consideran el mismo valor en conjuntos, por lo tanto, son tratados como duplicados")
my_tuple = ("apple", "banana", "cherry", True, 1, 2)
my_set = {"apple", "banana", "cherry", True, 1, 2}
print(f"intentado agregar los elementos True y 1 a un conjunto: {my_tuple}")
print(f"Conjunto resultante: {my_set}")
print('')

# Los valores False y 0 se consideran el mismo valor en conjuntos, por lo tanto, son tratados como duplicados:
print("Los valores False y 0 se consideran el mismo valor en conjuntos, por lo tanto, son tratados como duplicados")
my_tuple = ("apple", "banana", "cherry", False, 0, 2)
my_set = {"apple", "banana", "cherry", False, 0, 2}
print(f"intentado agregar los elementos False y 0 a un conjunto: {my_tuple}")
print(f"Conjunto resultante: {my_set}")
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# ACCEDIENDO A ELEMENTOS DE UN CONJUNTO
print("\nACCEDIENDO A ELEMENTOS DE UN CONJUNTO\n")

# No es posible acceder a elementos de un conjunto haciendo referencia a un índice o una clave. 
# Pero se pueden recorrer los elementos del conjunto usando un bucle for, o preguntar si un valor específico está presente en un conjunto, usando la palabra clave in.
thisset = {"apple", "banana", "cherry"}
print(f"Accediendo a los elementos del conjunto {thisset} usando un bucle for")
for x in thisset:
  print(f"Elemento del conjunto: {x}")
print(f"Preguntando si el elemento 'banana' esta presente en el conjunto {thisset}, Respuesta: {'banana' in thisset}")
print('')

# AGREGANDO ELEMENTOS A UN CONJUNTO
print("\nAGREGANDO ELEMENTOS A UN CONJUNTO\n")

# Una vez que se crea un conjunto, no es posible cambiar sus elementos, pero si es posible agregar elementos nuevos.
# El método add() permite agregar un elemento a un conjunto
print("El método add() se utiliza para agregar nuevos elementos a un conjunto")
thisset = {"apple", "banana", "cherry"}
print(f"Agregando el elemento 'orange' al conjunto: {thisset}")
thisset.add("orange")
print(f"Conjunto modificado: {thisset}")
print('')

# El método update() se utiliza para agregar elementos de un conjunto a otro.
print("El método update() se utiliza para agregar elementos de un conjunto a otro")
aux_set= {"mango", "lemon"}
print(f"Agregando los elementos de {aux_set} al conjunto: {thisset}")
thisset.update(aux_set)
print(f"Conjunto modificado: {thisset}")
print('')

# El método update() no solo permite agregar elementos de un conjunto a otros, sino que tambien, permite agregar cualquier objeto iterable a un conjunto (tuplas, listas, diccionarios, etc.)
# El método update() se utiliza para agregar elementos de un conjunto a otro.
print("El método update() tambien permite  agregar elementos de cualquier iterable a un conjunto")
thisset = {"apple", "banana", "cherry"}
aux_list= ["mango", "lemon"]
print(f"Agregando los elementos de {aux_list} al conjunto: {thisset}")
thisset.update(aux_list)
print(f"Conjunto modificado: {thisset}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ELIMINANDO ELEMENTOS DE UN CONJUNTO
print("\nELIMINANDO ELEMENTOS DE UN CONJUNTO\n")

# El método remove() se utiliza para eliminar un elemento específico de un conjunto.
# Este método elimina el elemento especificado del conjunto. Si el elemento no está presente en el conjunto, genera un error
print("El método remove() se utiliza para eliminar elementos de un conjunto.")
thisset = {"apple", "banana", "cherry"}
print(f"Eliminando el elemento 'banana' del conjunto: {thisset}")
thisset.remove("banana")
print(f"Conjunto modificado: {thisset}")
print('')

# El método discard() tambien permite eliminar un elemento de un conjunto.
# Este método también elimina el elemento especificado del conjunto. Sin embargo, si el elemento no está presente en el conjunto, no se produce ningún error.
print("El método remove() se utiliza para eliminar elementos de un conjunto.")
thisset = {"apple", "banana", "cherry"}
print(f"Eliminando el elemento 'banana' del conjunto: {thisset}")
thisset.discard("banana")
print(f"Conjunto modificado: {thisset}")
print('')

# El método pop() se utiliza para eliminar un elemento aleatorio de un conjunto y devuelve el resultado en una variable
# Este método eliminará un elemento aleatorio, por lo que no se puede estar seguro de qué elemento se elimina.
print("El método pop() se utiliza para eliminar un elemento en una posición aleatoria de un conjunto")
thisset = {"apple", "banana", "lemon", "cherry", "banana"}
print(f"Eliminando un elemento aleatorio del conjunto: {thisset}")
removed_item = thisset.pop()
print(f"Elemento eliminado: {removed_item}")
print(f"Conjunto modificado: {thisset}")
print('')

# El método clear() se utiliza para vaciar el contenido de un conjutno. El conjunto aún permanece, pero no tiene contenido.
print("El método clear() se utiliza para vaciar un conjunto")
thisset = {"apple", "banana", "lemon", "cherry", "banana"}
print(f"Eliminando el contenido del conjunto: {thisset}")
thisset.clear()
print(f"Conjunto modificado: {thisset}")
print('')

# Para eliminar un conjunto completamente, se utiliza la palabra clave del.
# Esto libera la memoria asociada con el conjunto, lo que puede ser útil en programas con grandes cantidades de datos
print("La palabra clave del se utiliza para eliminar completamente un conjunto.")
print(f"Eliminando el conjunto: {thisset}")
del thisset
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# RECORRIENDO ELEMENTOS DE UN CONJUNTO
print("\nRECORRIENDO ELEMENTOS DE UN CONJUNTO\n")

# PLa forma mas ampliamente utilizada para recorrer los elementos de un conjunto es utilizando un bucle for.
print("Recorriendo los elementos de un conjunto utilizando un bucle for.")
my_set = {"apple", "mango", "lemon", "banana"}
print(f"Los elementos del conjunto {my_set} son:")
for element in my_set:
    print(f'Elemento del conjunto: {element}')
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPERACION DE CONJUNTOS
print("\nOPERACION DE CONJUNTOS\n")

print("UNION DE CONJUNTOS\n")
# Hay varias formas de unir dos o más conjuntos en Python
# Los métodos union() y update() permiten realizar la union de dos o mas conjuntos.
# La union de conjuntos en python excluirá cualquier elemento duplicado.
print("Los métodos union() y update() permiten unir todos los elementos de dos o mas conjuntos")
myset1 = {1,2,3,4}
myset2 = {5,6,7,8}
print(f"Uniendo los conjuntos {myset1} y {myset2}")
unionset = myset1.union(myset2) # devuelve un nuevo conjunto
myset1.update(myset2)           # no devuelve nada
print(f"Resultado del metodo union(): {unionset}")
print(f"Resultado del metodo update(): {myset1}")
print('')

# La union tambien se puede realizar entre un conjunto y cualquier objeto iterable
print("La union tambien se puede realizar entre un conjunto y cualquier objeto iterable")
myset1 = {1,2,3,4}
mylist1 = [5,6,7,8]
unionset = myset1.union(mylist1)
print(f"Uniendo el conjunto {myset1} y la lista {mylist1} mediante el metodo union(), resultado: {unionset}")
print('')

# El operador | tambien permite realizar la union de conjuntos
# El operador | solo permite unir conjuntos con conjuntos, y no con otros tipos de datos como si es posible con el método union()
print("El operador | tambien permite realizar la union  de conjuntos")
myset1 = {1,2,3,4}
myset2 = {5,6,7,8}
unionset = myset1 | myset2
print(f"Uniendo los conjuntos {myset1} y {myset2} mediante el operador |, resultado: {unionset}")
print('')

print("INTERSECCIÓN DE CONJUNTOS\n")
# Los métodos intersection() y intersection_update() permiten realizar la intersección de dos o mas conjuntos.
# La interseccion de conjuntos en python mantiene solo los elementos duplicados.
print("Los métodos intersection() e intersection_update() mantienen solo los elementos duplicados de dos o mas conjuntos")
myset1 = {1,2,3,4}
myset2 = {3,4,5,6}
print(f"Intersectando los conjuntos {myset1} y {myset2}")
intersectionset = myset1.intersection(myset2)   # devuelve un nuevo conjunto
myset1.intersection_update(myset2)              # no devuelve nada
print(f"Resultado del metodo intersection(): {intersectionset}")
print(f"Resultado del metodo intersection_update(): {myset1}")
print('')

# El operador & tambien permite realizar la interseccion de conjuntos
# El operador & solo permite intersectar conjuntos con conjuntos, y no con otros tipos de datos como si es posible con el método intersection()
print("El operador & tambien permite realizar la inteserccion de conjuntos")
myset1 = {1,2,3,4}
myset2 = {3,4,5,6}
intersectionset = myset1 & myset2
print(f"La interseccion de los conjuntos {myset1} y {myset2} utilizando el operador & es: {intersectionset}")
print('')

print("DIFERENCIA DE CONJUNTOS\n")
# Los métodos difference() y difference_update() permiten realizar la diferencia de dos o mas conjuntos.
# La diferencia de conjuntos en python mantienen los elementos del primer conjunto que no están presentes en los demas conjuntos.
print("Los métodos difference() e difference_update() mantienen los elementos del primer conjunto que no están presentes en los demas conjuntos")
myset1 = {"apple", "banana", "cherry"}
myset2 = {"google", "microsoft", "apple"}
print(f"Diferencia entre los conjuntos {myset1} y {myset2}")
differenceset = myset1.difference(myset2)   # devuelve un nuevo conjunto
myset1.difference_update(myset2)            # no devuelve nada
print(f"Resultado del metodo difference(): {differenceset}")
print(f"Resultado del metodo difference_update(): {myset1}")
print('')

# El operador - tambien permite realizar la diferencia de conjuntos
# El operador - solo permite realizar la diferencia de conjuntos con conjuntos, y no con otros tipos de datos como si es posible con el método difference()
print("El operador - tambien permite realizar la diferencia de conjuntos")
myset1 = {1,2,3,4}
myset2 = {3,4,5,6}
differenceset = myset1 - myset2
print(f"La diferencia de los conjuntos {myset1} y {myset2} utilizando el operador - es: {differenceset}")
print('')

print("DIFERENCIA SIMETRICA DE CONJUNTOS\n")
# Los métodos symmetric_difference() y symmetric_difference_update() permiten realizar la diferencia simetrica de dos o mas conjuntos.
# La diferencia simetrica en python mantendrá solo los elementos que NO están presentes en los conjuntos
print("Los métodos symmetric_difference() e symmetric_difference_update() mantienen solo los elementos que NO están presentes en los conjuntos")
myset1 = {"apple", "banana", "cherry"}
myset2 = {"cherry", "microsoft", "apple"}
print(f"Diferencia simetrica entre los conjuntos {myset1} y {myset2}")
symmetricdifferenceset = myset1.symmetric_difference(myset2)    # devuelve un nuevo conjunto
myset1.symmetric_difference_update(myset2)                      # no devuelve nada
print(f"Resultado del metodo symmetric_difference(): {symmetricdifferenceset}")
print(f"Resultado del metodo symmetric_difference_update(): {myset1}")
print('')

# El operador ^ tambien permite realizar la diferencia simetrica de conjuntos
# El operador ^ solo permite realizar la diferencia simetrica de conjuntos con conjuntos, y no con otros tipos de datos como si es posible con el método symmetric_difference()
print("El operador ^ tambien permite realizar la diferencia simetrica de conjuntos")
myset1 = {1,2,3,4}
myset2 = {3,4,5,6}
symmetricdifferenceset = myset1 ^ myset2
print(f"La diferencia simetrica de los conjuntos {myset1} y {myset2} utilizando el operador ^ es: {symmetricdifferenceset}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# METODOS ADICIONALES DE CONJUNTOS
print("\nPRINCIPALES METODOS DE CONJUNTOS\n")

# El método len() determina cuántos elementos estan presentes en un conjunto
print("El metodo len() determina el número de elementos dentro de un conjunto")
set1 = {1,2,3,4,5}
print(f"el conjunto {set1} tiene un total de {len(set1)} elementos")
print('')

# El método copy() permite realizar una copia de un conjunto
print("El metodo copy() permite realizar una copia de un conjunto")
set1 = {"apple", "banana", "cherry"}
print(f"Conjunto original: {set1}")
copyset = set1.copy()
print(f"Conjunto copiado: {copyset}")
print('')

# El método isdisjoint() verifica si dos conjuntos son disjuntos.
# En otras palabras verifica si los conjuntos no tienen elementos en común.
print("El método isdisjoint() verifica si dos conjuntos no tienen elementos en común")
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(f"verificando si los conjuntos {set1} y {set2} tienen elementos en común, Respuesta: {set1.isdisjoint(set2)}")
print('')

# El método issubset() verifica si todos los elementos de un conjunto están presentes en otro conjunto.
# En otras palabras verifica si el primer conjunto es un subconjunto del segundo
print("El método issubset() verifica si un conjunto es subconjunto de otro")
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(f"verificando si el conjunto {set1} es subconjunto de {set2}, Respuesta: {set1.issubset(set2)}")
print('')

# El método issuperset() verifica si un conjunto contiene todos los elementos de otro conjunto.
# En otras palabras si el primer conjunto es un superconjunto del segundo
print("El método issuperset() verifica si un conjunto es superconjunto de otro")
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print(f"verificando si el conjunto {set1} es superconjunto de {set2}, Respuesta: {set1.issuperset(set2)}")
print('')

