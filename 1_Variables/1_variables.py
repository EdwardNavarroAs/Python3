# Tema 1: Variables en python
# las variables son contenedores para almacenar valores de datos
# Una variable se crea en el momento en el que se le asigna un valor por primera vez
print("una variable se crea en el momento que se le asigna un valor")
x1 = 5
x2 = "John"
print(f"variable 1 es: {x1}, variable 2 es {x2}")
print('')

# No es necesario declarar variables con ningún tipado en particular, incluso pueden cambiar de tipo 
# después de haber sido configuradas.
print("las variables pueden ser de cualquier tipo y pueden cambiar de tipo una vez declaradas")
x = 4       # x es de tipo entero (int)
print(x)
x = "Sally" # x es de tipo cadena de texto (str)
print(x)
print('')

# Si se desea especificar el tipo de datos de una variable, es posible hacerlo mediante palabras clave
print("especificando el tipo de una variable")
x = str(3)    
y = int(3)    
z = float(3) 
print(f"variable 1 {x} de tipo {type(x)}, variable 2 {y} de tipo {type(y)}, variable 3 {z} de tipo {type(z)}") 
print('')

# Los nombres de las variables distinguen entre mayúsculas y minúsculas.
print("variables distinguen de mayusculas y minusculas")
a = 4
A = "Sally"
print(f"variable a: {a}, es diferente de variable A: {A}")
print('')

# Reglas para nombrar variables en Python:
"""El nombre de una variable debe comenzar con una letra o un carácter de subrayado.
El nombre de una variable no puede comenzar con un número.
El nombre de una variable solo puede contener caracteres alfanuméricos y guiones bajos (Az, 0-9 y _).
Los nombres de las variables distinguen entre mayúsculas y minúsculas (edad, Edad y EDAD son variables diferentes)
Un nombre de variable no puede ser ninguna de las palabras clave de Python .

ej variables legales:               ej variables ilegales

myvar = "John"                      2myvar = "John"
my_var = "John"                     my-var = "John"
_my_var = "John"                    my var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
"""
print("nombrando variables en python")
# metodo Carmel: Cada palabra, excepto la primera, comienza con mayúscula (mas utilizada)
myVariableName = "myVariableName"
# metodo Pascal: Cada palabra comienza con una letra mayúscula
MyVariableName = "MyVariableName"
# metodo Snake: Cada palabra está separada por un guion bajo
my_variable_name = "my_variable_name"
print(f"metodo carmel: {myVariableName}, metodo pascal: {MyVariableName}, metodo snake: {my_variable_name}")
print('')

# Python permite asignar valores a múltiples variables en una sola línea
print("asignando multiples valores de variables")
x, y, z = "Orange", "Banana", "Cherry"
print(f"variable 1: {x}, variable 2: {y}, variable 3: {z}")
print('')

# python permite asignar el mismo valor a múltiples variables en una línea:
print("asignando el mismo valor a multiples variables")
x = y = z = 10
print(f"variable 1: {x}, variable 2: {y}, variable 3: {z}")
print('')
