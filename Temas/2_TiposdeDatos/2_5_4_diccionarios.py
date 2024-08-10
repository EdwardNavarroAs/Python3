# Tema 2: Tipos de datos en python
# 2.5.4 diccionarios

# Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.
# Un diccionario es una colección ordenada, modificable y que no permite duplicados.
#   --> los elementos de un diccionario tienen un orden definido y ese orden no cambiará.
#   --> Es posible cambiar, agregar y eliminar elementos a un diccionario después de haberlo creado.
#   --> Los diccionarios no pueden tener dos elementos con la misma clave, los valores duplicados sobrescribirán los valores existentes.
#   --> Los elementos de un diccionario se presentan en pares clave:valor y se puede hacer referencia a ellos mediante el nombre de la clave.

# ----------------------------------------------------------------------------------------------------------------------------------------
# DEFINIENDO UN DICCIONARIO EN PYTHON
print("\nDEFINIENDO DICCIONARIOS\n")

# Los diccionarios se definen utilizando llaves {} y tienen claves y valores
print("los diccionarios en en Python se definen utilizando llaves {} y sus elementos se definen mediante pares clave:valor")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"Diccionario en Python: {thisdict}, Tipo de dato: {type(thisdict)}")
print('')

# También se puede definir un diccionario utilizando el constructor dict()
print("También se puede definir un diccionario utilizando el constructor dict():")
thisdict = dict(name = "John", age = 36, country = "Norway")
print(f"Diccionario en Python: {thisdict}, Tipo de dato: {type(thisdict)}")
print('')

# Los diccionarios pueden contener cualquier tipo de dato, incluso otros diccionarios
print("Los diccionarios pueden contener cualquier tipo de dato:")
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"],
  "owner": {
      "name": 'juanito',
      "years": 32
  }
}
print(f"Diccionario con diferentes tipos de datos: {thisdict}")
print('')

# Los diccionarios no pueden tener dos elementos con la misma clave, los valores duplicados sobrescribirán los valores existentes:
print("Los diccionarios no permiten elementos duplicados, los valores duplicados sobreescribiran los valores existentes")
str_dict= "{'brand': 'Ford','model': 'Mustang','year': 1964,'year': 2020}"
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(f"intentado agregar claves duplicadas a un diccionario: {str_dict}")
print(f"Diccionario resultante: {thisdict}")
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# ACCEDIENDO A ELEMENTOS DE UN DICCIONARIO
print("\nACCEDIENDO A ELEMENTOS DE UN DICCIONARIO\n")

# Para determinar si una clave especifica está presente en un diccionario, se utiliza la palabra clave in.
print("Verificando si una clave específica se encuentra en un diccionario:")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
result = 'brand' in thisdict
print(f"Verificando si 'brand' se encuentra presente en el diccionario {thisdict}, resultado: {result}")
print('')

# Para acceder a los elementos de un diccionario se debe consultar su nombre clave, entre corchetes []. Sin embargo, si la clave no está presente en el diccionario se presentará un error.
print("Accediendo a elementos de un diccionario mediante su clave utilizando []")
print(f"El valor del elemento con palabra clave 'year' del diccionario {thisdict} es: {thisdict['year']}")
print('')

# El método get() permite obtener también los elementos de un diccionario a partir de su clave. Sin embargo, este método permite devolver un valor por defecto en caso de que dicha clave no exista.
print("El método get() se utiliza para acceder a elementos de un diccionario mediante su clave. Si la clave no existe se puede colocar un valor por defecto.")
print(f"El valor del elemento con palabra clave 'model' del diccionario {thisdict} es: {thisdict.get('model')}")
print(f"El valor del elemento con palabra clave 'owner' del diccionario {thisdict} es: {thisdict.get('owner', 'No encontrado')}")
print('')

# El método keys() permite obtener una lista de todas las claves presentes en un diccionario.
# La lista de claves es una vista del diccionario, lo que significa que cualquier cambio realizado en el diccionario se reflejará en la lista de claves.
print("El método keys() permite obtener una lista de todas las claves presentes en un diccionario.")
keys = thisdict.keys()
print(f"Las claves presentes en el diccionario {thisdict} son: {keys}")
print('')

# El método values() permite obtener una lista de todas los valores presentes en un diccionario.
# La lista de valores es una vista del diccionario, lo que significa que cualquier cambio realizado en el diccionario se reflejará en la lista de valores.
print("El método values() permite obtener una lista de todos los valores presentes en un diccionario.")
values = thisdict.values()
print(f"Los valores presentes en el diccionario {thisdict} son: {values}")
print('')

# El método items() permite obtener los elementos de un diccionario, como una lista de tuplas.
# La lista de elementos es una vista del diccionario, lo que significa que cualquier cambio realizado en el diccionario se reflejará en la lista de elementos.
print("El método items() permite obtener los elementos de un diccionario como una lista de tuplas.")
items = thisdict.items()
print(f"Los elementos (items) presentes en el diccionario {thisdict} son: {items}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CAMBIANDO ELEMENTOS DE UN DICCIONARIO
print("\nCAMBIANDO ELEMENTOS DE UN DICCIONARIO\n")

# Para cambiar el valor de un elemento en un diccionario, se debe consultar su clave.
print("Para cambiar el valor de un elemento en una lista, se debe consultar su clave.")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"Cambiando el elemento con clave 'year' del diccionario: {thisdict}")
thisdict['year'] = 1980
print(f"Diccionario modificado: {thisdict}")
print('')

# El método update() permite actualizar un diccionario con los elementos del argumento dado. El argumento debe ser un diccionario o un objeto iterable con pares clave:valor.
# Si la clave no existe, se creará en el diccionario.
print("El método update() se utiliza para actualizar un diccionario con otro iterable con pares clave:valor.")
iterable = {"year": 2020}
print(f"Actualizando el diccionario {thisdict} con el iterable {iterable}")
thisdict.update(iterable)
print(f"Diccionario modificado: {thisdict}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# AGREGANDO ELEMENTOS A UN DICCIONARIO
print("\nAGREGANDO ELEMENTOS A UN DICCIONARIO\n")

# Para agregar un nuevo elemento a un diccionario se debe crear una nueva clave y asignarle un valor.
print("Para agregar un nuevo elemento a un diccionario se debe crear una nueva clave con su valor correspondiente.")
print(f"Agregando el elemento 'owner':'jose' al diccionario {thisdict}")
thisdict['owner'] = 'jose'
print(f"Diccionario modificado: {thisdict}")
print('')

# El método update() también permite agregar nuevos elementos a un diccionario existente. El argumento debe ser un diccionario o un objeto iterable con pares clave:valor.
print("El método update() también se puede utilizar para agregar nuevos elementos a un diccionario existente.")
iterable = {"color": 'red'}
print(f"Agregando el iterable {iterable} al diccionario {thisdict}")
thisdict.update(iterable)
print(f"Diccionario modificado: {thisdict}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ELIMINANDO ELEMENTOS DE UN DICCIONARIO
print("\nELIMINANDO ELEMENTOS DE UN DICCIONARIO\n")

# El método pop() elimina el elemento con el nombre de clave especificado
print("El método pop() se utiliza para eliminar un elemento específico mediante su clave.")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"Eliminando el elemento con clave 'model' del diccionario {thisdict}")
thisdict.pop("model")
print(f"Diccionario modificado: {thisdict}")
print('')

# El método popitem() elimina el último elemento de un diccionario
print("El método popitem() elimina el último elemento de un diccionario.")
print(f"Eliminando el último elemento del diccionario {thisdict}")
thisdict.popitem()
print(f"Diccionario modificado: {thisdict}")
print('')

# La palabra clave 'del' elimina el elemento con el nombre de clave especificado
print("La palabra clave 'del' elimina el elemento con el nombre de clave especificado.")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"Eliminando el elemento con clave 'model' del diccionario {thisdict}")
del thisdict["model"]
print(f"Diccionario modificado: {thisdict}")
print('')

# El método clear() se utiliza para vaciar el contenido de un diccionario. El diccionario aún permanece, pero no tiene contenido.
print("El método clear() se utiliza para vaciar un diccionario.")
print(f"Eliminando el contenido del diccionario: {thisdict}")
thisdict.clear()
print(f"Diccionario modificado: {thisdict}")
print('')

# Para eliminar un diccionario completamente, se utiliza la palabra clave del.
# Esto libera la memoria asociada, lo que puede ser útil en programas con grandes cantidades de datos.
print("La palabra clave del también se utiliza para eliminar completamente un diccionario.")
print(f"Eliminando el diccionario: {thisdict}")
del thisdict
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# RECORRIENDO ELEMENTOS DE UN DICCIONARIO
print("\nRECORRIENDO ELEMENTOS DE UN DICCIONARIO\n")

# Para recorrer los elementos de un diccionario, se puede utilizar un bucle for.
# Al recorrer un diccionario mediante este método, solo se obtienen las claves del diccionario.
print("Recorriendo las claves de un diccionario utilizando un bucle for.")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"Las claves del diccionario {thisdict} son:")
# Nota: el enumerate no es necesario, solo es para generar un contador
for i, key in enumerate(thisdict):
    print(f'clave {i+1}: {key}')
print('')

# Para recorrer los valores del diccionario mediante un bucle for, se debe acceder a cada uno de los elementos mediante su clave respectiva.
print("Recorriendo los valores de un diccionario utilizando un bucle for.")
print(f"Los valores del diccionario {thisdict} son:")
# Nota: el enumerate no es necesario, solo es para generar un contador
for i, key in enumerate(thisdict):
    print(f'valor {i+1}: {thisdict[key]}')
print('')

# Es posible usar el método values() para obtener los valores de un diccionario.
print("Recorriendo los valores de un diccionario utilizando el método values().")
print(f"Los valores del diccionario {thisdict} son:")
# Nota: el enumerate no es necesario, solo es para generar un contador
for i, value in enumerate(thisdict.values()):
    print(f'valor {i+1}: {value}')
print('')

# Es posible usar el método keys() para obtener las claves de un diccionario.
print("Recorriendo las claves de un diccionario utilizando el método keys().")
print(f"Las claves del diccionario {thisdict} son:")
# Nota: el enumerate no es necesario, solo es para generar un contador
for i, key in enumerate(thisdict.keys()):
    print(f'clave {i+1}: {key}')
print('')

# Es posible usar el método items() para obtener los elementos de un diccionario.
print(f"Los elementos del diccionario {thisdict} son:")
# Nota: el enumerate no es necesario, solo es para generar un contador
for i, element in enumerate(thisdict.items()):
    print(f'elemento {i+1}: ({element[0]}, {element[1]})')
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# COMPRENSIÓN DE DICCIONARIOS EN PYTHON
print("\nCOMPRENSIÓN DE DICCIONARIOS EN PYTHON\n")

# La comprensión de diccionarios ofrece una sintaxis más corta cuando se desea crear un nuevo diccionario basado en los 
# valores de un iterable existente.
# Sintaxis:
# newdict = {key: value for item in iterable if condition == True}
# El valor de retorno es un diccionario nuevo, que deja la lista original sin cambios.

# Utilizando la comprensión de diccionarios para crear nuevos diccionarios bajo condiciones específicas.
print("Utilizando la comprensión de diccionarios para crear un nuevo diccionario.")
fruits = {'fruit1': "apple", 'fruit2': "banana", 'fruit3': "cherry", 'fruit4':"kiwi"}
print(f"diccionario original: {fruits}")
fruits_with_a = {key: value for key, value in fruits.items() if "a" in value}
fruits_without_kiwi = {key: value for key, value in fruits.items() if value != "kiwi"}
print(f"Diccionario solo con elementos que contengan la letra 'a': {fruits_with_a}")
print(f"Diccionario excluyendo el elemento 'kiwi': {fruits_without_kiwi}")
print('')

# El iterable puede ser cualquier objeto iterable, como una lista, tupla, conjunto, etc.
print("El iterable puede ser cualquier objeto iterable.")
print("Utilizando la comprensión de diccionarios y la función range() para crear diccionarios de números enteros.")
digit_dict = {digit: digit + 1 for digit in range(10)}
digit_dict_less_than_5 = {digit: digit + 1 for digit in range(10) if digit < 5}
print(f"Diccionario con números del 0 al 9 mapeados a números del 1 al 10: {digit_dict}")
print(f"Diccionario con números del 0 al 4 mapeados a números del 1 al 5: {digit_dict_less_than_5}")
print()

# En la sintaxis de comprensión de diccionarios, la expresión es el par clave-valor actual en la iteración, 
# que también es el resultado y puede ser manipulado antes de ser añadido al nuevo diccionario.
print("La expresión representa los pares clave-valor resultado que contendrá el nuevo diccionario, los cuales pueden ser manipulados.")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_upper = {fruit: fruit.upper() for fruit in fruits}
print(f"Lista original: {fruits}")
print(f"Diccionario con frutas en mayúsculas: {fruits_upper}")
print()

# En la sintaxis de comprensión de diccionarios, la expresión también puede contener condiciones, no solo como un filtro,
# sino como una forma de manipular el resultado.
print("La expresión puede contener condiciones como una forma de manipular el resultado.")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newdict = {fruit: (fruit if fruit != "banana" else "lemon") for fruit in fruits}
print(f"Lista original: {fruits}")
print(f"Diccionario manipulado: {newdict}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# COPIANDO UN DICCIONARIO
print("\nCOPIANDO UN DICCIONARIO\n")

# No es posible copiar un diccionario simplemente escribiendo dict2 = dict1, porque: dict2 solo será una referencia a dict1, 
# y los cambios realizados en dict1 también se realizarán automáticamente en dict2.

# Una de las formas correctas de hacer una copia de un diccionario es utilizar el método copy().
print("Utilizando el método copy() para copiar un diccionario.")
print(f"Diccionario original: {thisdict}")
thisdict_copy = thisdict.copy()
print(f"Diccionario copiado: {thisdict_copy}")
print('')

# Otra forma de hacer una copia de un diccionario es utilizando el método integrado dict()
print("Utilizando el método dict() para copiar un diccionario.")
print(f"Diccionario original: {thisdict}")
thisdict_copy2 = dict(thisdict)
print(f"Diccionario copiado: {thisdict_copy2}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DICCIONARIOS ANIDADOS
# Un diccionario puede contener diccionarios, lo que se denomina diccionarios anidados.
print("Un diccionario puede contener otros diccionarios, lo que se conoce como diccionarios anidados.")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print("Ejemplo de un diccionario anidado:")
print(myfamily)
print('')

# Otra manera de hacer un diccionario anidado es agregar los diccionarios independientes dentro de un nuevo diccionario
print("Un diccionario anidado puede ser creado a partir de diccionarios independientes.")
child1 = {
  "name" : "Emily",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
print(f"Los diccionarios independientes son:")
print(f"Dict1: {child1}")
print(f"Dict2: {child2}")
myfamily = {
  "child1" : child1,
  "child2" : child2,
}
print("El diccionario anidado resultante es:")
print(myfamily)
print('')

# Para acceder a los elementos de un diccionario anidado se debe consultar el nombre clave de los diccionarios,
# comenzando con el diccionario más grande 
print("Para acceder a elementos de un diccionario anidado se debe utilizar el nombre clave de los diccionarios.")
print(f"El nombre del segundo hijo del diccionario {myfamily} es: {myfamily['child2']['name']}")
print('')

# Tambien es posible acceder a un elemento de un diccionario anidado utilizando el método get()
print("tambien es posible acceder a elementos de un diccionario anidado utilizando el método get().")
child2_name = myfamily.get("child1").get("name")
print("El nombre del primer hijo es:", child2_name)
print('')

# También es posible recorrer un diccionario anidado utilizando el método items():
print("Para recorrer un diccionario anidado se puede utilizar el método items().")
print(f"Recorriendo el diccionario: {myfamily}")
for children, attributes in myfamily.items():
  for attribute in attributes:
    print(attribute + ':', attributes[attribute])
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# METODOS ADICIONALES DE DICCIONARIOS
print("\nPRINCIPALES METODOS DE LISTAS\n")

# El método len() determina cuántos elementos estan presentes en un diccionario
print("El metodo len() determina cuantos elementos estan presentes en un diccionario")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"El diccionario {thisdict} tiene un total de {len(thisdict)} elementos")
print('')

# el método fromkeys() permite crear un diccionario con las claves y el valor especificados.
print("El metodo fromkeys() permite crear un diccionario con las claves y el valor especificados.")
x = ('key1', 'key2', 'key3')
y = 10
print("las claves del diccionario son: ", x)
print("los valores del diccionario son: ", y)
thisdict2 = dict.fromkeys(x, y)
print(f"diccionario creado con el metodo fromkeys(): ", thisdict2)
print('')

# el método setdefault() devuelve el valor de la clave especificada. Si la clave no existe: se inserta la clave, con el valor especificado
print("El método setdefault() devuelve el valor de la clave especificada. Si la clave no existe: se inserta la clave, con el valor especificado")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
model = car.setdefault("model")
print(f"el valor de la clave 'model' del diccionario {car} es: {model}")
color = car.setdefault("color", 'red')
print(f"el valor de la clave 'color' del diccionario {car} es: {color}")
# Nota en este caso el diccionario original tambien es alterado

