# ------------------------------------------------------------------------------------------------
# Tema 8_3: Expresiones regulares en Python
# ------------------------------------------------------------------------------------------------

# Una expresión regular (RegEx) es una secuencia de caracteres que forma un patrón de búsqueda.
# RegEx se puede utilizar para comprobar si una cadena contiene el patrón de búsqueda especificado.
# Python tiene un paquete incorporado llamado re, que se utiliza para trabajar con expresiones regulares.
import re

# Ejemplo 1: Comprueba si la cadena de texto empieza con "La" y termina con "Colombia":
txt = "La lluvia en Colombia"
x = re.search("^La.*Colombia$", txt)

if x:
  print("¡SÍ! ¡Tenemos una coincidencia!")
else:
  print("No hay coincidencia")

# El módulo re ofrece un conjunto de funciones que permiten buscar una coincidencia en una cadena de texto:
"""
Nombre de la función     |   Descripción de la función
---------------------------------------------------------------------------------------------------------------
findall                  |   Devuelve una lista que contiene todas las coincidencias                          |
search                   |   Devuelve un objeto Match si hay una coincidencia en cualquier parte de la cadena |
split                    |   Devuelve una lista donde la cadena se ha dividido en cada coincidencia           |
sub                      |   Reemplaza una o varias coincidencias con una cadena                              |
"""

# Los metacaracteres son caracteres con un significado especial en las expresiones regulares:
"""
Carácter  |        Descripción                | Ejemplo
---------------------------------------------------------------------------------------------------------------
    []    | Encuentra cualquier carácter de   | "[a-m]" Encuentra todas las letras de la 'a' a la 'm'.
          | un conjunto de caracteres         |
---------------------------------------------------------
    \     | Escapa caracteres especiales o    | "\d" Encuentra cualquier dígito (equivale a [0-9]).
          | señala una secuencia especial     | "\\." Encuentra un punto literal en la cadena.
---------------------------------------------------------
    .     | Encuentra cualquier carácter      | "he..o" Encuentra cualquier cadena que comience con "he" y
          | excepto una nueva línea           | termine con "o" con dos caracteres en medio.
---------------------------------------------------------
    ^     | Indica que la búsqueda debe       | "^hola" Encuentra todas las cadenas que comiencen con "hola".
          | empezar con el patrón especificado|
---------------------------------------------------------
    $     | Indica que la búsqueda debe       | "mundo$" Encuentra todas las cadenas que terminen con "mundo".
          | terminar con el patrón especificado|
---------------------------------------------------------
    *     | Encuentra cero o más ocurrencias  | "ho.*a" Encuentra cualquier cadena que empiece con "ho" y
          | del patrón especificado           | termine con "a", con cualquier cantidad de caracteres en medio.
---------------------------------------------------------
    +     | Encuentra una o más ocurrencias   | "ho.+a" Encuentra cualquier cadena que empiece con "ho" y
          | del patrón especificado           | termine con "a", con al menos un carácter en medio.
---------------------------------------------------------
    ?     | Encuentra cero o una ocurrencia   | "ho.?a" Encuentra "hoa" o "ho-a", pero solo una vez o ninguna.
          | del patrón especificado           |
---------------------------------------------------------
    {}    | Encuentra un número exacto de     | "ho.{2}a" Encuentra cualquier cadena que comience con "ho",
          | ocurrencias del patrón            | seguida de exactamente dos caracteres y termine con "a".
---------------------------------------------------------
    |     | Indica una elección entre         | "llueve|soleado" Encuentra cadenas que contengan "llueve"
          | patrones posibles (o bien, o bien)| o "soleado".
---------------------------------------------------------
    ()    | Agrupa patrones y captura los     | "ho(la|la)" Encuentra "hola" o "holla", agrupando las opciones
          | resultados dentro del grupo       | entre paréntesis.
"""

