# ------------------------------------------------------------------------------------------------
# Tema 8: Módulos en Python
# ------------------------------------------------------------------------------------------------

# Un módulo en Python se considera lo mismo que una biblioteca de código. Es decir, un archivo que contiene un 
# conjunto de funciones, variables, o clases que pueden ser reutilizadas en otras partes de una aplicación.

# ------------------------------------------------------------------------------------------------
# CREACIÓN DE UN MÓDULO EN PYTHON
# Un módulo es un archivo que contiene funciones, variables o clases, y que puede ser utilizado por otros archivos.
# Para crear un módulo, simplemente guarda el código que deseas reutilizar en un archivo con extensión .py.

# Para usar un módulo en otro archivo, debes importarlo usando la declaración import:
import mymodule

print("\nCREACIÓN DE MÓDULOS EN PYTHON\n")
print("Un módulo en Python es un archivo que contiene funciones, variables o clases que pueden ser utilizados por otros módulos.")
print("Ejemplo de un llamado a un módulo externo desde un archivo principal:")
mymodule.greeting("Edward")
print('')

# ------------------------------------------------------------------------------------------------
# VARIABLES EN EL MÓDULO
# Un módulo puede contener funciones, como ya se ha descrito, pero también variables de todo tipo (listas, diccionarios, objetos, etc.).
print("\nVARIABLES EN MÓDULOS\n")

a = mymodule.person1["age"]
print("Un módulo puede contener funciones, como también variables de todo tipo (listas, diccionarios, objetos, etc.).")
print("Ejemplo de llamado a una variable guardada en un módulo desde un archivo principal:")
print(f"Variable guardada en el módulo: {a}")
print('')

# ------------------------------------------------------------------------------------------------
# REENOMBRANDO MÓDULOS
# En Python, se puede cambiar el nombre de un módulo mediante un alias cuando se importe un módulo, utilizando la palabra reservada as:
import mymodule as mx

a = mx.person1["name"]
print("\nREENOMBRANDO MÓDULOS\n")
print("Es posible renombrar un módulo utilizando la palabra clave 'as'.")
print("Ejemplo de llamado a una variable guardada en un módulo desde un archivo principal utilizando un alias:")
print(f"Variable guardada en el módulo: {a}")
print('')

# ------------------------------------------------------------------------------------------------
# MÓDULOS INTEGRADOS
# Hay varios módulos integrados en Python que pueden ser importados cuando se requiera.
# Por ejemplo, el módulo 'platform' se utiliza para recuperar información sobre la plataforma en la que se está ejecutando actualmente el programa.
import platform

x = platform.system()
print("\nMÓDULOS INTEGRADOS\n")
print("Python incluye varios módulos integrados que pueden ser importados cuando sean necesarios.")
print("Por ejemplo, el módulo 'platform' revela información sobre la plataforma en la que se está ejecutando el programa:")
print(f"El sistema operativo donde se está ejecutando el programa es: {x}")
print('')

# ------------------------------------------------------------------------------------------------
# FUNCIÓN DIR()
# La función dir() permite enumerar todos los nombres de funciones (o nombres de variables) que están presentes en un módulo.
# Esto es útil para descubrir qué funciones y variables están disponibles en un módulo.
print("\nFUNCIÓN DIR()\n")
x = dir(platform)
print("La función dir() enumera todos los nombres de funciones o variables presentes en un módulo.")
print("Enumerando todas las funciones y variables presentes en el módulo 'platform':")
print(x)
print('')

# ------------------------------------------------------------------------------------------------
# IMPORTAR DESDE UN MÓDULO
# En Python, es posible elegir importar solo partes de un módulo utilizando la palabra clave 'from'.
# Esto permite importar solo las funciones o variables que necesitas, en lugar de importar todo el módulo.
# Nota: Al importar utilizando 'from', no utilices el nombre del módulo al hacer referencia a los elementos importados.
from mymodule import person1

print("\nIMPORTAR CÓDIGO ESPECÍFICO DESDE UN MÓDULO\n")
a = person1["country"]
print("En Python es posible importar solo partes de un módulo utilizando la palabra clave 'from'.")
print("Ejemplo de llamado a una variable específica guardada en un módulo desde un archivo principal:")
print(f"Variable guardada en el módulo: {a}")
print('')

# ------------------------------------------------------------------------------------------------
# PAQUETES EN PYTHON
# Un paquete en Python es una manera de estructurar una colección de módulos relacionados.
# Un paquete se crea colocando los módulos en un directorio con un archivo __init__.py.
# Es posible importar módulos desde el paquete utilizando:
from mypackage import modulo1

# O también importar funciones específicas:
from mypackage.modulo2 import my_function

# Esto permite una organización más limpia y modular del código.


# ------------------------------------------------------------------------------------------------
# MÓDULOS ESPECIALES
# Python tiene un módulo especial llamado '__main__' que permite ejecutar código solo cuando un archivo es ejecutado directamente,
# y no cuando es importado como un módulo.

print("\nMÓDULOS ESPECIALES\n")
print("Python tiene un módulo especial llamado '__main__' que permite ejecutar código solo cuando el archivo es ejecutado directamente")

if __name__ == "__main__":
    print("Este código solo se ejecutará si este archivo es ejecutado directamente, no cuando se importa como módulo.")
    print('')

# ------------------------------------------------------------------------------------------------
# MANEJO DE ERRORES EN IMPORTACIÓN
# Si se intenta importar un módulo que no existe, Python lanzará un ImportError.
# Puedes manejar esto usando un bloque try-except:

print("\nMANEJO DE ERRORES EN IMPORTACIÓN\n")
print("Si se intenta importar un módulo que no existe, Python lanzará un ImportError")

try:
    print("intentando importar un módulo inexistente...")
    import nonexistentmodule
except ImportError:
    print("Error: El módulo no pudo ser encontrado.")
