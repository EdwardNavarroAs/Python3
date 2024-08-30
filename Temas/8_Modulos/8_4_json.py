# ------------------------------------------------------------------------------------------------
# Tema 8_2: Archivos JSON en Python
# ------------------------------------------------------------------------------------------------

# JSON (JavaScript Object Notation) es un formato ligero para almacenar e intercambiar datos.
# JSON es texto escrito en una sintaxis que sigue la notación de objetos de JavaScript,
# lo que lo hace fácil de leer y escribir tanto para humanos como para máquinas.

# ------------------------------------------------------------------------------------------------
# MÓDULO JSON EN PYTHON
# Python tiene un paquete incorporado llamado json, que puede usarse para trabajar con datos JSON.
print("\nMÓDULO JSON EN PYTHON\n")
import json

# Convertir de JSON a Python
# En Python es posible convertir una cadena JSON en un objeto Python utilizando el método json.loads().
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

print("El método json.loads() permite convertir una cadena JSON a un objeto Python.")
print(f"Convirtiendo la cadena JSON ({x}, {type(x)}) en un diccionario ({y}, {type(y)})")
print('')

# Convertir de Python a JSON
# En Python se puede convertir un objeto Python a una cadena JSON utilizando el método json.dumps().
# Nota:
#   - Es posible convertir objetos Python de los siguientes tipos en cadenas JSON: dict, list, tuple, string, int, float, True, False, None
x1 = {"name": "John", "age": 30}
x2 = ("apple", "bananas")
x3 = "hello"
x4 = 42
x5 = 31.76
x6 = True
x7 = None

y1 = json.dumps(x1)
y2 = json.dumps(x2)
y3 = json.dumps(x3)
y4 = json.dumps(x4)
y5 = json.dumps(x5)
y6 = json.dumps(x6)
y7 = json.dumps(x7)

print("El método json.dumps() permite convertir un objeto Python a una cadena JSON.")
print(f"Convirtiendo un diccionario ({x1}, {type(x1)}) en una cadena JSON ({y1}, {type(y1)})")
print(f"Convirtiendo una tupla ({x2}, {type(x2)}) en una cadena JSON ({y2}, {type(y2)})")
print(f"Convirtiendo una cadena de texto ({x3}, {type(x3)}) en una cadena JSON ({y3}, {type(y3)})")
print(f"Convirtiendo un entero ({x4}, {type(x4)}) en una cadena JSON ({y4}, {type(y4)})")
print(f"Convirtiendo un flotante ({x5}, {type(x5)}) en una cadena JSON ({y5}, {type(y5)})")
print(f"Convirtiendo un booleano ({x6}, {type(x6)}) en una cadena JSON ({y6}, {type(y6)})")
print(f"Convirtiendo un None ({x7}, {type(x7)}) en una cadena JSON ({y7}, {type(y7)})")
print('')

# Al convertir de Python a JSON, los objetos de Python se convierten en su equivalente en JSON:
"""
    Python  | JSON
    ------- | -----
    dict    | Object
    list    | Array
    tuple   | Array
    str     | String
    int     | Number
    float   | Number
    True    | true
    False   | false
    None    | null
"""

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y = json.dumps(x)

print("El método json.dumps() permite convertir un objeto complejo de Python a una cadena JSON.")
print(f"Convirtiendo un diccionario anidado ({x}, {type(x)}) en una cadena JSON ({y}, {type(y)})")
print('')

