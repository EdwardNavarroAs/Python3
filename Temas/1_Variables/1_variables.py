# Tema 1: Variables en Python

# DEFINICIÓN DE VARIABLES
# Las variables son contenedores para almacenar valores de datos.
# Una variable se crea en el momento en el que se le asigna un valor por primera vez.
print("\nDEFINICIÓN DE UNA VARIABLE EN PYTHON\n")
print("Una variable se crea en el momento que se le asigna un valor")
x1 = 5
x2 = "John"
print(f"Variable 1 es: {x1}, variable 2 es {x2}")
print('')

# ------------------------------------------------------------------------------------------------
# PYTHON NO ES UN LENGUAJE TIPADO
# No es necesario declarar variables con ningún tipo en particular; incluso pueden cambiar de tipo 
# después de haber sido configuradas.
print("\nPYTHON NO ES UN LENGUAJE TIPADO\n")
print("Las variables pueden ser de cualquier tipo y pueden cambiar de tipo una vez declaradas")
x = 4       # x es de tipo entero (int)
print(f"Variable x: {x} es del tipo {type(x)}")
x = "Sally" # x es de tipo cadena de texto (str)
print(f"Variable x: {x} ahora es del tipo {type(x)}")
print('')

# Si se desea especificar el tipo de datos de una variable, es posible hacerlo mediante funciones de conversión.
print("Especificando el tipo de una variable")
x = str(3)    
y = int(3)    
z = float(3) 
print(f"Variable 1 con valor: '{x}', es de tipo {type(x)}; variable 2 con valor: '{y}', es de tipo {type(y)}; variable 3 con valor: {z}, es de tipo {type(z)}") 
print('')

# ------------------------------------------------------------------------------------------------
# NOMBRES DE LAS VARIABLES SON SENSIBLES A MAYÚSCULAS Y MINÚSCULAS
# Los nombres de las variables distinguen entre mayúsculas y minúsculas.
print("\nLAS VARIABLES SON SENSIBLES A MAYÚSCULAS Y MINÚSCULAS\n")
print("Las variables en Python distinguen entre mayúsculas y minúsculas")
a = 4
A = "Sally"
print(f"Variable a: {a}, es diferente de variable A: {A}")
print('')

# ------------------------------------------------------------------------------------------------
# NOMBRE DE VARIABLES
# Reglas para nombrar variables en Python:
"""
El nombre de una variable debe comenzar con una letra o un carácter de subrayado.
El nombre de una variable no puede comenzar con un número.
El nombre de una variable solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _).
Los nombres de las variables distinguen entre mayúsculas y minúsculas (edad, Edad y EDAD son variables diferentes).
Un nombre de variable no puede ser ninguna de las palabras clave de Python.

Ejemplos de variables legales:      Ejemplos de variables ilegales:
myvar = "John"                      2myvar = "John"
my_var = "John"                     my-var = "John"
_my_var = "John"                    my var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
"""
print("\nEXISTEN DIFERENTES MÉTODOS PARA NOMBRAR VARIABLES EN PYTHON\n")
# Método camelCase: Cada palabra, excepto la primera, comienza con mayúscula (más utilizado)
myVariableName = "myVariableName"
# Método PascalCase: Cada palabra comienza con una letra mayúscula
MyVariableName = "MyVariableName"
# Método snake_case: Cada palabra está separada por un guion bajo
my_variable_name = "my_variable_name"
print("Los métodos más utilizados son:")
print(f"Método camelCase: {myVariableName}, método PascalCase: {MyVariableName}, método snake_case: {my_variable_name}")
print('')

# ------------------------------------------------------------------------------------------------
# ASIGNACIÓN DE VARIABLES
# Python permite asignar valores a múltiples variables en una sola línea
print("\nASIGNACIÓN DE VARIABLES\n")
print("Asignando múltiples valores a variables")
x, y, z = "Orange", "Banana", "Cherry"
print(f"Variable 1: {x}, variable 2: {y}, variable 3: {z}")
print('')

# Python permite asignar el mismo valor a múltiples variables en una línea
print("Asignando el mismo valor a múltiples variables")
x = y = z = 10
print(f"Variable 1: {x}, variable 2: {y}, variable 3: {z}")
print('')

# ------------------------------------------------------------------------------------------------
# VARIABLES LOCALES Y GLOBALES
# Una variable global es accesible desde cualquier parte del código.
x = "global"

def myfunc():
    # Una variable local solo es accesible dentro de la función.
    x = "local"
    print("Variable que se accede dentro de una función:", x)

print("\nVARIABLES LOCALES Y GLOBALES EN PYTHON\n")
print("Una variable local solo es accesible dentro de una función, mientras que una variable global es accesible desde cualquier parte")
myfunc()
# Fuera de la función, la variable global sigue siendo accesible.
print("Variable que se accede fuera de una función:", x)
print('')

# Uso de la palabra clave 'global'
# La palabra clave 'global' permite modificar una variable global dentro de una función.
print("Uso de la palabra clave 'global'")
print("La palabra clave global permite modificar una variable global dentro de una función")
y = "global"

def myfunc_global():
    global y
    # Ahora la variable global será modificada dentro de esta función y se mantendrá ese valor en el resto del código
    y = "modificada globalmente"
    print("Dentro de la función:", y)

myfunc_global()
# Fuera de la función, la variable global ha sido modificada.
print("Fuera de la función:", y)
print('')

# ------------------------------------------------------------------------------------------------
# PALABRA CLAVE NONLOCAL
# La palabra clave nonlocal se utiliza para trabajar con variables dentro de funciones anidadas.
# La palabra clave nonlocal permite modificar una variable en la función externa desde una función anidada.
def myfunc1():
    x = "Variable local de la función myfunc1"
    def myfunc2():
        nonlocal x
        x = "Variable modificada en la función anidada myfunc2"
    myfunc2()
    return x

print("\nPALABRA CLAVE NONLOCAL EN PYTHON\n")
print("La palabra clave nonlocal se utiliza para trabajar con variables dentro de funciones anidadas, permitiendo modificar una variable en la función externa desde una función anidada.")
print(myfunc1())
print('')

# ------------------------------------------------------------------------------------------------
# DESEMPAQUETADO EN PYTHON
# Python permite el desempaquetado de secuencias, lo que significa asignar elementos de una secuencia 
# (como listas o tuplas) a múltiples variables de manera simultánea.
print("\nDESEMPAQUETADO DE SECUENCIAS EN PYTHON\n")

fruits = ["apple", "banana", "cherry"]

# Desempaqueta la secuencia en tres variables diferentes
x, y, z = fruits

print("Python permite asignar elementos de una secuencia a múltiples variables de forma simultánea")
print(f"Variable 1: {x}, variable 2: {y}, variable 3: {z}")
print('')

# Si el número de elementos de la secuencia es mayor que el número de variables, se debe utilizar '*' en la última variable para capturar los valores restantes
data = [1, 2, 3, 4, 5]
first, *rest = data
print("Si el número de elementos de la secuencia es mayor que el número de variables, se debe utilizar '*' en la última variable para capturar los valores restantes")
print(f"Primer valor: {first}, Valores restantes: {rest}")
print('')

# ------------------------------------------------------------------------------------------------
# VARIABLES DE CLASE E INSTANCIA

# En Python, las clases pueden tener dos tipos principales de variables:
# - Variables de clase: Estas son compartidas entre todas las instancias de la clase.
# - Variables de instancia: Estas son específicas de una instancia particular de la clase.

print("\nVARIABLES DE CLASE E INSTANCIA\n")
print("Las variables de clase son compartidas entre todas las instancias de la clase, mientras que las variables de instancia son específicas de una instancia particular de la clase")
# Definimos una clase con una variable de clase y una variable de instancia
class MyClass:
    # Variable de clase: se define directamente en la clase
    class_variable = "Soy una variable de clase"

    def __init__(self, instance_variable):
        # Variable de instancia: se define dentro del método __init__
        self.instance_variable = instance_variable

obj = MyClass("Soy una variable de instancia")
print(f"Variable de clase: {MyClass.class_variable}")
print(f"Variable de instancia: {obj.instance_variable}")
print('')

# ------------------------------------------------------------------------------------------------
# VARIABLES ESPECIALES EN PYTHON

# En Python, hay varias variables y convenciones especiales que se utilizan para distintos propósitos.
# Estas incluyen variables como __name__ y __main__, que son útiles para la ejecución de scripts y módulos.

print("\nVARIABLES ESPECIALES EN PYTHON\n")
print("En Python, hay varias variables especiales que se utilizan para distintos propósitos, como __name__ y __main__, las cuales son utilizadas para la ejecución de scripts y módulos.")
print("la variable __name__ indica el nombre del módulo actual")
# La variable especial __name__ indica el nombre del módulo actual.
# Cuando un script se ejecuta directamente, __name__ toma el valor "__main__".
# Si el script es importado como un módulo en otro script, __name__ toma el valor del nombre del módulo.

if __name__ == "__main__":
    # Este bloque de código se ejecuta solo si el script se está ejecutando directamente.
    # No se ejecutará si el script es importado como un módulo en otro script.
    print("Este bloque de código se ejecuta solo si el script se está ejecutando directamente")

print('')
