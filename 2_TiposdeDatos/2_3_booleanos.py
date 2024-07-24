# Tema 2: Tipos de datos en python
# 2.3 Boleanos

# Los booleanos representan uno de dos valores posibles: True o False.
# En python se puede evaluar cualquier expresión y obtener una de dos posibles respuestas: True o False
print("Evaluando expresiones booleanas")
print(f"evaluando la expresion 10 > 9: ", 10 > 9)
print(f"evaluando la expresion 10 == 9: ", 10 == 9)
print(f"evaluando la expresion 10 < 9: ", 10 < 9)
print('')

# La función bool() permite evaluar cualquier valor y devolver True o False
# En donde, la mayoria de valores son verdaderos:
    # Casi cualquier valor es True si tiene algún tipo de contenido.
    # Cualquier cadena es True, excepto las cadenas vacías.
    # Cualquier número es True, excepto el 0.
    # Cualquier lista, tupla, conjunto y diccionario son True, excepto si estan vacíos

print("evaluando la funcion bool() de python")
print(f"evaluando una cadena de texto con contenido: ", bool("abc"))
print(f"evaluando un número entero: ", bool(123))
print(f"evaluando una lista: ", bool(["apple", "cherry", "banana"]))
print(f"evaluando el valor False", bool(False))
print(f"evaluando el valor None: ",bool(None))
print(f"evaluando el número 0: ", bool(0))
print(f"evaluando una cadena de texto vacia: ", bool(""))
print(f"evaluando una lista vacia: ", bool([]))
print('')

# Python tiene funciones integradas que devuelven un valor booleano: 
    # La función isinstance(), se puede utilizar para determinar si un objeto es de un determinado tipo de datos
print("evaluando la función isinstance() de python")
x = 10
print(f"evaluando si un numero es del tipo entero: ", isinstance(x, int))
print('')
