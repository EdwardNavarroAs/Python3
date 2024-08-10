# Tema 3: Condicionales en Python

# Las sentencias condicionales también se denominan sentencias de decisión. Se utilizan para ejecutar un bloque específico 
# de código si las condiciones dadas son verdaderas o falsas, permitiendo controlar el flujo de ejecución del programa 
# y ejecutar determinados conjuntos de sentencias solo cuando se cumple una condición.

# ----------------------------------------------------------------------------------------------------------------------------------------
# Condicional "IF"
# La sentencia «If» permite ejecutar un bloque de código si se cumple una condición específica. 
# Se comprueba la condición y el conjunto de código del bloque «If» se ejecuta si es verdadera. 
# De lo contrario, el código del bloque «If» no se ejecuta y se ejecuta la sentencia que sigue a la sentencia If. 
# En ambos casos, cualquier línea de código fuera de la sentencia se evalúa por defecto.
# Python utiliza la indentación para especificar el bloque de código que debe ejecutarse cuando se cumpla la condición.
print("\nSENTENCIA CONDICIONAL IF\n")

print('Utilizando la sentencia condicional "IF" en Python')
a, b = 33, 200
print(f"Evaluando si {b} es > que {a}")
if b > a:
   print("La condición if se cumple")
   print(f"{b} es mayor que {a}")
print('')

# En Python es posible ejecutar una sentencia if en una sola línea de código, 
# siempre y cuando solo tenga una única declaración (línea de código) que cumpla la condición. Esto se conoce como abreviación de una sentencia if (Short Hand If).
print('Utilizando la abreviación de la sentencia condicional "IF" en Python')
print(f"Evaluando si {b} es > que {a}")
if b > a: print(f"{b} es mayor que {a}")
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# Condicional "IF-ELSE"
# La sentencia «If-else» se utiliza para ejecutar tanto la parte verdadera como la falsa de una condición. 
# Si la condición es verdadera, se ejecuta el bloque de código situado debajo de la sentencia If. Por otro lado, si los resultados 
# de la expresión de prueba son falsos, se ejecuta el bloque de código situado debajo de la sentencia Else.
# Se debe tener en cuenta que solo se puede cumplir una de las dos condiciones y en ambos casos se utiliza la indentación para definir el alcance del código.
print("\nSENTENCIA CONDICIONAL IF-ELSE\n")

print('Utilizando la sentencia condicional "IF-ELSE" en Python')
a, b = 200, 33
print(f"Evaluando si {b} es mayor o igual que {a}")
if b >= a:
   print("La condición if se cumple")
   print(f"{b} es mayor o igual que {a}")
else:
   print("La condición else se cumple")
   print(f"{a} es mayor que {b}")
print('')

# En Python es posible ejecutar una sentencia if-else en una sola línea de código,
# siempre y cuando solo tenga una única declaración (línea de código) que cumpla la condición (verdadera o falsa).
# Esta técnica se conoce como Operadores Ternarios o Expresiones Condicionales.
print('Utilizando la abreviación de la sentencia condicional "IF-ELSE", también conocido como operador ternario en Python')
a, b = 33, 200
print(f"Evaluando si {b} es mayor que {a}")
print(f"{a} es mayor o igual que {b}") if a >= b else print(f"{b} es mayor que {a}")

# También es posible tener varias declaraciones else en una misma línea. Esta técnica se conoce como operador ternario múltiple
print('Utilizando el operador ternario múltiple para evaluar varias condiciones en una única línea de código')
print(f"{a} es mayor que {b}") if a > b else print(f"{a} es igual a {b}") if a == b else print(f"{b} es mayor que {a}")
print('')

# ----------------------------------------------------------------------------------------------------------------------------------------
# Condicional "ELIF"
# La palabra clave elif es la forma en que Python dice "si las condiciones anteriores no eran verdaderas, intenta la siguiente condición".
# Se utiliza en el caso de un problema condicional múltiple.
# En primer lugar, se comprueba la condición de la sentencia If. Si es falsa, se evalúa la sentencia Elif. Si la condición Elif también es falsa, se evalúa la sentencia Else.
print("\nSENTENCIA CONDICIONAL ELIF\n")

print('Utilizando la sentencia condicional "ELIF" en Python')
a = b = 33
print(f"Evaluando si {b} es mayor o igual que {a}")
if b > a:
   print("La condición if se cumple")
   print(f"{b} es mayor que {a}")
elif a == b:
   print("La condición elif se cumple")
   print(f"{a} y {b} son iguales")
else:
   print("La condición else se cumple")
   print(f"{b} es menor que {a}")
print('')

# Para probar varias expresiones, se puede utilizar una cadena de sentencias Elif, lo que se denomina «Elif ladder» (escalera Elif). 
# El controlador comprueba las condiciones de la sentencia If, y si se cumplen, se ejecuta el conjunto de sentencias de ese bloque.
# En caso contrario, el controlador pasa al primer bloque Elif para evaluar las condiciones. El proceso continúa para todas las sentencias Elif
# y si se determina en la evaluación que todas las condiciones If y Elif son falsas, se ejecuta el bloque Else.
print('Utilizando la escalera "ELIF" en Python')
a = b = 100
print(f"Evaluando si {a} es mayor, igual o menor que {b}")
if b > a:
   print("La condición if se cumple")
   print(f"{b} es mayor que {a}")
elif b < a:
   print("La primera condición elif se cumple")
   print(f"{b} es menor que {a}")
elif a == b:
   print("La segunda condición elif se cumple")
   print(f"{a} y {b} son iguales")
else:
   print("La condición else se cumple")
print('')

# En Python es posible tener declaraciones if dentro de otras, lo que se conoce como declaraciones if anidadas.
print("Utilizando las declaraciones if anidadas para evaluar múltiples condiciones")
x = 41
print(f"Evaluando si el número {x} está en un rango específico")
if x > 10:
    print(f"{x} está por encima de 10")
    if x > 20:
        print(f"{x} está también por encima de 20")
    else:
        print(f"pero {x} no está por encima de 20")
print('')
