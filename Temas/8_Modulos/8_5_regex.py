# ------------------------------------------------------------------------------------------------
# Tema 8_3: Expresiones regulares en Python
# ------------------------------------------------------------------------------------------------

# Una expresión regular (RegEx) es una secuencia de caracteres que forma un patrón de búsqueda.
# RegEx se puede utilizar para comprobar si una cadena contiene el patrón de búsqueda especificado.

# El módulo re ofrece un conjunto de funciones que permiten buscar una coincidencia en una cadena de texto:
"""
Nombre de la función     |   Descripción de la función
---------------------------------------------------------------------------------------------------------------
findall                  |   Devuelve una lista que contiene todas las coincidencias                          |
search                   |   Devuelve un objeto Match si hay una coincidencia en cualquier parte de la cadena |
split                    |   Devuelve una lista donde la cadena se ha dividido en cada coincidencia           |
sub                      |   Reemplaza una o varias coincidencias con una cadena                              |
"""

# Los metacaracteres avanzados incluyen secuencias como lookahead y lookbehind:
"""
Carácter  |        Descripción                          | Ejemplo
---------------------------------------------------------------------------------------------------------------
    []    | Encuentra cualquier carácter de un conjunto| "[a-m]" Encuentra todas las letras de la 'a' a la 'm'.
---------------------------------------------------------------------------------------------------------------
    \     | Escapa caracteres especiales o señala una   | "\d" Encuentra cualquier dígito (equivale a [0-9]).
          | secuencia especial                         | "\\." Encuentra un punto literal en la cadena.
---------------------------------------------------------------------------------------------------------------
    .     | Cualquier carácter excepto nueva línea      | "he..o" Encuentra cualquier cadena que empiece con "he"
          |                                             | y termine con "o", con dos caracteres en medio.
---------------------------------------------------------------------------------------------------------------
    ^     | Empieza con                                 | "^hola" Encuentra todas las cadenas que comiencen con "hola".
---------------------------------------------------------------------------------------------------------------
    $     | Termina con                                 | "mundo$" Encuentra todas las cadenas que terminen con "mundo".
---------------------------------------------------------------------------------------------------------------
    *     | Cero o más ocurrencias                      | "ho.*a" Encuentra cualquier cadena que empiece con "ho"
          |                                             | y termine con "a", con cualquier cantidad de caracteres en medio.
---------------------------------------------------------------------------------------------------------------
    +     | Una o más ocurrencias                       | "ho.+a" Encuentra cualquier cadena que empiece con "ho"
          |                                             | y termine con "a", con al menos un carácter en medio.
---------------------------------------------------------------------------------------------------------------
    ?     | Cero o una ocurrencia                       | "ho.?a" Encuentra "hoa" o "ho-a", pero solo una vez o ninguna.
---------------------------------------------------------------------------------------------------------------
    {}    | Exactamente el número especificado de       | "ho.{2}a" Encuentra cualquier cadena que comience con "ho",
          | ocurrencias                                 | seguida de exactamente dos caracteres y termine con "a".
---------------------------------------------------------------------------------------------------------------
    |     | O bien, o bien                              | "llueve|soleado" Encuentra cadenas que contengan "llueve"
          |                                             | o "soleado".
---------------------------------------------------------------------------------------------------------------
    ()    | Agrupa y captura                            | "ho(la|la)" Encuentra "hola" o "holla", agrupando las opciones.
---------------------------------------------------------------------------------------------------------------
    (?=...) | Lookahead positivo                        | "ho(?=la)" Encuentra "ho" solo si está seguido por "la".
---------------------------------------------------------------------------------------------------------------
    (?!...) | Lookahead negativo                        | "ho(?!la)" Encuentra "ho" solo si no está seguido por "la".
---------------------------------------------------------------------------------------------------------------
    (?<=...) | Lookbehind positivo                      | "(?<=hola) mundo" Encuentra "mundo" solo si está precedido por "hola".
---------------------------------------------------------------------------------------------------------------
    (?<!...) | Lookbehind negativo                      | "(?<!hola) mundo" Encuentra "mundo" solo si no está precedido por "hola".
"""

# Una secuencia especial es un \ seguido de uno de los caracteres de la lista siguiente, 
# y tiene un significado especial en las expresiones regulares:

"""
Carácter  |        Descripción                                  | Ejemplo
---------------------------------------------------------------------------------------------------------------
    \A    | Devuelve una coincidencia si los caracteres         |  "\AThe" Coincide si la cadena comienza con "The".
          | especificados están al principio de la cadena       |  Ejemplo: re.search("\AThe", "The rain in Spain")
---------------------------------------------------------------------------------------------------------------
    \b    | Devuelve una coincidencia si los caracteres         |  r"\bain" Coincide si "ain" está al principio o
          | especificados están al principio o al final de una  |  r"ain\b" Coincide si "ain" está al final de la palabra.
          | palabra (la "r" garantiza que la cadena se trate    |  Ejemplo: re.search(r"\bain", "ain es mi palabra favorita")
          | como una "cadena sin formato")                      |           re.search(r"ain\b", "Esta es la palabra ain")
---------------------------------------------------------------------------------------------------------------
    \B    | Devuelve una coincidencia donde los caracteres      |  r"\Bain" Coincide si "ain" NO está al principio o al
          | especificados están presentes, pero NO al principio |  r"ain\B" final de una palabra.
          | o al final de una palabra                           |  Ejemplo: re.search(r"\Bain", "La palabra pain está en medio")
---------------------------------------------------------------------------------------------------------------
    \d    | Devuelve una coincidencia donde la cadena contiene  |  "\d" Coincide con cualquier dígito (números del 0 al 9).
          | dígitos (números del 0 al 9)                        |  Ejemplo: re.search("\d", "Hay 3 gatos en casa")
---------------------------------------------------------------------------------------------------------------
    \D    | Devuelve una coincidencia donde la cadena NO        |  "\D" Coincide si NO hay dígitos en la cadena.
          | contiene dígitos                                    |  Ejemplo: re.search("\D", "El gato duerme")
---------------------------------------------------------------------------------------------------------------
    \s    | Devuelve una coincidencia donde la cadena contiene  |  "\s" Coincide con cualquier carácter de espacio en blanco.
          | un carácter de espacio en blanco                    |  Ejemplo: re.search("\s", "Hola Mundo")
---------------------------------------------------------------------------------------------------------------
    \S    | Devuelve una coincidencia donde la cadena NO        |  "\S" Coincide con cualquier carácter que NO sea un espacio.
          | contiene un carácter de espacio en blanco           |  Ejemplo: re.search("\S", " Hola")
---------------------------------------------------------------------------------------------------------------
    \w    | Devuelve una coincidencia donde la cadena contiene  |  "\w" Coincide con cualquier carácter de palabra 
          | cualquier carácter de palabra (letras de la a a la  |  (letras, dígitos y el carácter de guión bajo).
          | Z, dígitos del 0 al 9 y el carácter de guión bajo _) |  Ejemplo: re.search("\w", "Python_3")
---------------------------------------------------------------------------------------------------------------
    \W    | Devuelve una coincidencia donde la cadena NO        |  "\W" Coincide con cualquier carácter que NO sea un carácter
          | contiene caracteres de palabra                      |  de palabra.
          |                                                     |  Ejemplo: re.search("\W", "¡Hola!")
---------------------------------------------------------------------------------------------------------------
    \Z    | Devuelve una coincidencia si los caracteres         |  "\Z" Coincide si la cadena termina con los caracteres
          | especificados están al final de la cadena           |  especificados.
          |                                                     |  Ejemplo: re.search("mundo\Z", "Hola mundo")
---------------------------------------------------------------------------------------------------------------
"""

# Un conjunto es un grupo de caracteres dentro de corchetes [], que define una clase de caracteres con un significado especial:
"""
Carácter    |        Descripción                                    
----------------------------------------------------------------------------
  [arn]     | Devuelve una coincidencia si alguno de los caracteres especificados 
            | (a, r o n) está presente en la cadena.
            | Ejemplo: re.search("[arn]", "python")
----------------------------------------------------------------------------
  [a-n]     | Devuelve una coincidencia para cualquier carácter en minúscula, 
            | alfabéticamente entre a y n.
            | Ejemplo: re.search("[a-n]", "python")
----------------------------------------------------------------------------
  [^arn]    | Devuelve una coincidencia para cualquier carácter EXCEPTO a, r y n.
            | Ejemplo: re.search("[^arn]", "python")
----------------------------------------------------------------------------
  [0123]    | Devuelve una coincidencia si alguno de los dígitos especificados 
            | (0, 1, 2 o 3) está presente.
            | Ejemplo: re.search("[0123]", "hay 2 gatos")
----------------------------------------------------------------------------
  [0-9]     | Devuelve una coincidencia para cualquier dígito entre 0 y 9.
            | Ejemplo: re.search("[0-9]", "hay 3 perros")
----------------------------------------------------------------------------
 [0-5][0-9] | Devuelve una coincidencia para cualquier número de dos dígitos entre 00 y 59.
            | Ejemplo: re.search("[0-5][0-9]", "La hora es 12:45")
----------------------------------------------------------------------------
  [a-zA-Z]  | Devuelve una coincidencia para cualquier carácter alfabético entre a y z, 
            | ya sea en minúsculas o mayúsculas.
            | Ejemplo: re.search("[a-zA-Z]", "Python3")
----------------------------------------------------------------------------
  [+]       | En los conjuntos, los caracteres especiales como +, *, ., |, (), $, {} 
            | pierden su significado especial. Por lo tanto, [+] significa: devolver 
            | una coincidencia para el carácter + literal en la cadena.
            | Ejemplo: re.search("[+]", "1 + 2 = 3")
----------------------------------------------------------------------------
"""


# Python tiene un paquete incorporado llamado re, que se utiliza para trabajar con expresiones regulares.
import re

# La función findall() devuelve una lista que contiene todas las coincidencias:
txt = "La lluvia en Colombia"

x = re.findall("ia", txt)
print("La función findall() devuelve una lista con todas las coincidencias en una cadena de texto.")
print(f'Generando una lista con todas las coincidencias de "ia" en la cadena de texto "{txt}":')
print(x)
print('')

# La función search() busca una coincidencia en la cadena y devuelve un objeto Match si hay una coincidencia.
# Si hay más de una coincidencia, solo se devolverá la primera ocurrencia:
x = re.search("\s", txt)

print("La función search() busca una coincidencia en la cadena y devuelve un objeto Match si hay una coincidencia.")
print(f'El primer espacio en blanco en la cadena de texto "{txt}" está en la posición: {x.start()}')
print('')

# La función split() devuelve una lista donde la cadena se ha dividido en cada coincidencia:
x = re.split("\s", txt)
print("La función split() devuelve una lista donde la cadena se ha dividido en cada coincidencia.")
print(f'Generando una lista donde la cadena de texto "{txt}" se ha dividido en cada carácter de espacio en blanco:')
print(x)
print('')

# También es posible controlar el número de ocurrencias especificando el parámetro maxsplit:
x = re.split("\s", txt, 1)
print("La función split() también permite especificar el número de ocurrencias mediante el parámetro maxsplit.")
print(f'Generando una lista dividiendo la cadena de texto "{txt}" solo en la primera aparición del carácter de espacio en blanco:')
print(x)
print('')

# La función sub() reemplaza las coincidencias con el texto elegido:
x = re.sub("\s", "9", txt)
print("La función sub() reemplaza las coincidencias con el texto elegido.")
print(f'Reemplazando cada carácter de espacio en blanco en la cadena de texto "{txt}" con el número 9:')
print(x)
print('')

# También es posible controlar el número de reemplazos especificando el parámetro de conteo:
x = re.sub("\s", "9", txt, 2)
print("La función sub() también permite especificar el número de reemplazos.")
print(f'Reemplazando los dos primeros caracteres de espacio en blanco en la cadena de texto "{txt}" con el número 9:')
print(x)
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OBJETO MATCH
# Un objeto Match es un objeto que contiene información sobre la búsqueda y el resultado.
#   Nota: Si no hay ninguna coincidencia, se devolverá el valor None en lugar de un objeto Match.
txt = "La lluvia en Colombia"
x = re.search("ia", txt)
print("Un objeto Match es un objeto que contiene información sobre la búsqueda y el resultado.")
print("Realizando una búsqueda que devuelve un objeto Match:")
print(f"Resultado: {x}, tipo de dato: {type(x)}")
print('')

# El objeto Match tiene propiedades y métodos que se utilizan para recuperar información sobre la búsqueda y el resultado:
# El método span() devuelve una tupla que contiene las posiciones de inicio y fin de la coincidencia
x = re.search(r"\bC\w+", txt)
print("El método span() devuelve una tupla que contiene las posiciones de inicio y fin de la coincidencia.")
print(f"Utilizando el método span() para obtener la posición (posición inicial y final) de la primera coincidencia dentro del texto '{txt}' que comience con la letra C mayúscula:")
print(x.span())
print('')

# La propiedad string devuelve la cadena pasada a la función
print("La propiedad string devuelve la cadena pasada a la función:")
print(x.string)
print('')

# El método group() devuelve la parte de la cadena donde hubo una coincidencia
print("El método group() devuelve la parte de la cadena donde hubo una coincidencia:")
print(x.group())
print('')

# ------------------------------------------------------------------------------------------------
# FLAGS O MODIFICADORES DE BÚSQUEDA

# Los flags permiten modificar el comportamiento de las expresiones regulares:
# re.IGNORECASE (re.I) permite hacer coincidir sin distinguir entre mayúsculas y minúsculas.
x = re.search(r"colombia", txt, re.IGNORECASE)
print("Usando re.IGNORECASE para hacer coincidir sin distinguir entre mayúsculas y minúsculas:")
print(f"Resultado al buscar 'colombia' en '{txt}': {x.group()}")
print('')

# re.DOTALL (re.S) hace que el punto (.) coincida también con nuevas líneas.
txt_multiline = "Lluvia\nColombia"
x = re.search(r"Lluvia.*Colombia", txt_multiline, re.DOTALL)
print("Usando re.DOTALL para que el punto coincida también con saltos de línea:")
print(f"Resultado al buscar 'Lluvia.*Colombia' en texto multilínea:\n{x.group()}")
print('')

# re.MULTILINE (re.M) permite que ^ y $ coincidan al inicio y fin de cada línea.
txt_multiline = "Lluvia en Bogotá\nColombia es hermoso"
x = re.findall(r"^Colombia", txt_multiline, re.MULTILINE)
print("Usando re.MULTILINE para que ^ coincida al inicio de cada línea:")
print(f"Coincidencias encontradas al buscar 'Colombia' al inicio de cada línea:\n{x}")
print('')

# ------------------------------------------------------------------------------------------------
# EJEMPLO COMPLETO UTILIZANDO CONJUNTOS, SECUENCIAS Y METACARACTERES

txt = "La lluvia en Bogotá, Colombia es maravillosa."
print('Ejemplo completo para encontrar un patrón en una cadena de texto:')
x = re.search(r"^La.*Colombia", txt)

if x:
    print("¡SÍ! ¡Existe una coincidencia!")
    print(f"El resultado es: {x.group()}")
else:
    print("No hay coincidencia..")