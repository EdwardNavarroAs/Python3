# ------------------------------------------------------------------------------------------------
# Tema 8_3: Expresiones regulares en Python
# ------------------------------------------------------------------------------------------------

# Una expresión regular (RegEx) es una secuencia de caracteres que forma un patrón de búsqueda.
# RegEx se puede utilizar para comprobar si una cadena contiene el patrón de búsqueda especificado.
# Python tiene un paquete incorporado llamado re, que se utiliza para trabajar con expresiones regulares.
import re

# Ejemplo 1: Comprueba si la cadena de texto empieza con "The" y termina con "Spain":
txt = "The rain in Colombia"
x = re.search("^The.*Colombia$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
