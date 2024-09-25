# Tema 9: Excepciones en Python

# Cuando ocurre un error, o una excepción como la llamamos, Python normalmente se detiene y genera un mensaje de error.
# Las excepciones en Python se manejan mediante diferentes bloques:

"""
El bloque try permite probar un bloque de código para detectar errores.

El bloque except permite gestionar el error que se haya producido.

El bloque else permite ejecutar código cuando no hay ningún error.

El bloque finally permite ejecutar código, independientemente de si se produjo o no una excepción.
"""

# Ejemplo 1 de manejo de excepciones: una variable no definida.
# Dado que el bloque try genera un error, se ejecuta el bloque except.
# Sin el bloque try, el programa se detiene y genera un error:
try:
    print("try permite probar un bloque de código para detectar errores.")
    print("Ejemplo 1: Intentando ejecutar un bloque de código donde una variable no está definida.")
    print(x)  # Esto causará una excepción ya que x no está definida
except:
    print("Error: Ha ocurrido una excepción general.")
    print('')

# Es posible definir tantos bloques de excepción como sea necesario, por ejemplo, 
# si es necesario ejecutar un bloque de código especial para un tipo específico de error:
try:
    print("Es posible definir tantos bloques de excepción como sea necesario.")
    print("Ejemplo 2: Manejando una excepción específica cuando una variable no está definida.")
    print(x)  # Esto causará una excepción
except NameError:
    print("Error: la variable no ha sido definida.")
    print('')
except:
    print("Error: Ha ocurrido una excepción general.")
    print('')

# En Python es posible utilizar la palabra clave else para definir un bloque de código que se ejecuta 
# solo si no se produjeron errores:
try:
    print("La palabra clave else se utiliza para definir un bloque de código que se ejecuta si no se produce ningún error.")
    print("Ejemplo 3: Uso de la palabra else en un bloque de código que no genera ninguna excepción.")
except:
    print("Error: Ha ocurrido una excepción general.")
    print('')
else:
    print("No se ha generado ninguna excepción.")
    print("Se ejecuta el bloque else.")
    print('')

# El bloque finally, si se especifica, se ejecuta independientemente de si el bloque try genera un error o no.
try:
    print("El bloque finally se ejecuta independientemente de si el bloque try genera un error o no.")
    print("Ejemplo 4: Ejecutando un bloque finally independientemente de si se genera una excepción en el código.")
    print(x)  # Esto causará una excepción
except:
    print("Error: Ha ocurrido una excepción general.")
finally:
    print("El bloque try-except ha finalizado.")
    print('')

# El bloque finally se utiliza comúnmente para cerrar objetos y limpiar recursos: 
try:
    print("El bloque finally se utiliza comúnmente para cerrar objetos y limpiar recursos.")
    print("Ejemplo 5: Utilizando el bloque finally para cerrar objetos o recursos abiertos.")
    f = open("demofile.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Error: Ha ocurrido una excepción al escribir en el archivo de texto.")
    finally:
        f.close()
except:
    print("Error: Ha ocurrido una excepción al abrir el archivo de texto.")
finally:
    print("El programa puede continuar sin dejar abierto el archivo.")
    print('')

# En Python, es posible generar una excepción si se cumplen ciertas condiciones.
# Para generar una excepción, se debe utilizar la palabra clave raise.
try:
    print("Es posible generar una excepción si se cumplen ciertas condiciones utilizando la palabra raise.")
    print("Ejemplo 6: Utilizando la palabra raise para generar una excepción general.")
    x = -1
    if x < 0:
        raise Exception("Error: El código no permite números negativos.")
except Exception as e:
    print("Error: Ha ocurrido una excepción general: ", str(e))
    print('')

# Es posible definir qué tipo de error generar y el texto que se mostrará al usuario.
try:
    print("La palabra raise permite definir el tipo de error generado y el texto presentado al usuario.")
    print("Ejemplo 7: Utilizando la palabra raise para generar una excepción específica.")
    
    x = "hello"
    
    if not type(x) is int:
        raise TypeError("Error: El código solo permite números enteros.")
except TypeError as e:
    print("Error: Ha ocurrido un error de tipado: ", str(e))
    print('')
except Exception as e:
    print("Error: Ha ocurrido una excepción general: ", str(e))
    print('')

# En Python es posible capturar múltiples excepciones en una sola línea utilizando una tupla.
try:
    print("El bloque try permite capturar múltiples excepciones en una sola línea.")
    print("Ejemplo 8: Captura de múltiples excepciones en una sola línea")
    print(z)
except (NameError, TypeError):
    print("Error: Ha ocurrido un NameError o un TypeError.")
    print('')

# También es posible crear excepciones personalizadas para definir errores específicos.
class MiExcepcionPersonalizada(Exception):
    pass

try:
    print("En Python es posible crear excepciones personalizadas para definir errores específicos.")
    print("Ejemplo 9: Excepciones personalizadas")
    raise MiExcepcionPersonalizada("Este es un error personalizado")
except MiExcepcionPersonalizada as e:
    print(f"Se ha generado una excepción personalizada: {e}")
    print('')

# La palabra clave as permite capturar detalles de una excepción.
try:
    print("La palabra clave 'as' permite capturar detalles de una excepción.")
    print("Ejemplo 10: Uso de 'as' para capturar el objeto de la excepción")
    division = 1 / 0
    print(division)
except ZeroDivisionError as e:
    print(f"Error: {e}")
    print('')

# En Python es posible encadenar excepciones para mostrar que un error fue causado por otro, utilizando el encadenamiento de excepciones con 'raise from'.
def validar_edad(edad):
    try:
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
    except ValueError as e:
        # Relanzar la excepción con un mensaje más específico
        raise ValueError("Ocurrió un error en la validación de la edad.") from e

try:
    print("En Python es posible encadenar excepciones para mostrar que un error fue causado por otro con 'raise from'.")
    print("Ejemplo 11: Encadenamiento de excepciones con 'raise from'")
    validar_edad(-5)
except ValueError as e:
    print(f"Error capturado: {e}")
    print(f"Excepción original: {e.__cause__}")
    print('')

# El módulo logging permite registrar excepciones de una manera más profesional.
import logging
logging.basicConfig(level=logging.ERROR)

try:
    print("El módulo logging permite registrar excepciones de una manera más profesional.")
    print("Ejemplo 12: Uso de logging para registrar excepciones")
    division = 1 / 0
    print(division)
except ZeroDivisionError as e:
    logging.error("Se produjo un error de división por cero", exc_info=True)
    print('')
