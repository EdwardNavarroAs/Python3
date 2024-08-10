# Tema 2: Tipos de datos en python
# 2.4 Operadores

# Los operadores se utilizan para realizar operaciones con variables y valores
# Python divide los operadores en los siguientes grupos:
    # Operadores aritméticos
    # Operadores de comparación
    # Operadores logicos
    # Operadores de identidad
    # Operadores de membresía
    # Operadores bit a bit
    # Operadores de Asignación


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPERADORES ARITMETICOS
print("\nOPERADORES ARITMÉTICOS\n")

# Los operadores aritméticos se utilizan con valores numéricos para realizar operaciones matemáticas.
x, y = 10, 2
print("uso de operadores aritméticos en python")
print(f"adición: {x} + {y} = {x+y}")
print(f"subtracción: {x} - {y} = {x-y}")
print(f"multiplicación: {x} * {y} = {x*y}")
print(f"división: {x} / {y} = {x/y}")
print(f"adición: {x} + {y} = {x+y}")
print(f"modulo: {x} % {y} = {x%y}") # obtiene el residuo de la división
print(f"exponenciación: {x} ** {y} = {x**y}")
print(f"floor division: {x} // {y} = {x//y}")   # redondea el resultado al número entero más cercano
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPERADORES DE COMPARACIÓN
print("\nOPERADORES DE COMPARACIÓN\n")

# Los operadores de comparación se utilizan para comparar dos varriables.
print("uso de operadores de comparación en python")
print(f"operador igual que (==):  {x} == {y} --> {x==y}")
print(f"operador diferente que (!=):  {x} != {y} --> {x!=y}")
print(f"operador mayor que (>):  {x} > {y} --> {x>y}")
print(f"operador menor que (<):  {x} < {y} --> {x<y}")
print(f"operador mayor igual que (>=):  {x} >= {y} --> {x>=y}")
print(f"operador menor igual que (<=):  {x} <= {y} --> {x<=y}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPERADORES LÓGICOS
print("\nOPERADORES LÓGICOS\n")

# Los operadores lógicos se utilizan para combinar declaraciones condicionales.
x1, y1 = 5, 2
x2, y2 = 10, 3
print("uso de operadores logicos en python")
print(f"operador (and) devuelve verdadero si todas las afirmaciones son verdaderas ({x1} > {y1}) and ({x2} < {y2}) --> {(x1>y1)and(x1<y2)}")
print(f"operador (or) devuelve verdadero si cualquiera de las afirmaciones son verdaderas ({x1} > {y1}) or ({x2} < {y2}) --> {(x1>y1)or(x1<y2)}")
print(f"operador (not) invierte el resultado, devuelve false si el resultado es verdadero not ({x1} > {y1})  --> {not(x1>y1)}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPERADORES DE IDENTIDAD
print("\nOPERADORES DE IDENTIDAD\n")

# Los operadores de identidad se utilizan para comparar los objetos, no si son iguales, sino si en realidad 
# son el mismo objeto, con la misma ubicación de memoria
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print("uso de operadores de identidad en python")
print(f"operador (is) devuelve true si ambas variables es el mismo objeto: ")
print(f"{x} is {z} --> {x is z}")
print(f"{x} is {y} --> {x is y}")
print(f"operador (is not) devuelve true si ambas variables no son el mismo objeto: ")
print(f"{x} is {z} --> {x is not z}")
print(f"{x} is {y} --> {x is not y}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPERADORES DE MEMBRESIA
print("\nOPERADORES DE MEMBRESIA\n")

# Los operadores de membresía se utilizan para probar si una secuencia esta presente en un objeto.
x = ["apple", "banana"]
print("uso de operadores de membresia en python")
print(f"operador (in) devuelve True si una secuencia con el valor especificado está presente en el objeto:")
print(f"banana in {x} --> {'banana'in x}")
print(f"operador (not in) devuelve True si una secuencia con el valor especificado no está presente en el objeto:")
print(f"orange not in {x} --> {'orange' not in x}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPERADORES BIT A BIT
print("\nOPERADORES BIT A BIT\n")

# Los operadores bit a bit se utilizan para comparar números (binarios)
x = 0b110
y = 0b011
z = 2 

print("uso de operadores bit a bit")
print(f"operador bit a bit and (&) compara cada bit y lo establece en 1 si ambos son 1; de lo contrario, se establece en 0:")
print(f"{bin(x)} & {bin(y)} --> {bin(x&y)}")
print(f"operador bit a bit or (|) compara cada bit y lo establece en 1 si uno o ambos son 1; de lo contrario, se establece en 0:")
print(f"{bin(x)} | {bin(y)} --> {bin(x|y)}")
print(f"operador bit a bit xor (^) compara cada bit y lo establece en 1 si uno de los dos es 1; de lo contrario (si ambos son 1 o ambos son 0) se establece en 0:")
print(f"{bin(x)} ^ {bin(y)} --> {bin(x^y)}")
print(f"operador bit a bit not (~) invierte cada bit (0 se convierte en 1 y 1 se convierte en 0:")
print(f"~ {bin(x)} --> {bin(~x)}")
print(f"operador bit a bit desplazamiento a la izquierda (<<) inserta el número especificado de ceros desde la derecha corriendo los bits hacia la izquierda:")
print(f"{bin(x)} << {z} --> {bin(x<<z)}")
print(f"operador bit a bit desplazamiento a la derecha (>>) inserta el número especificado de ceros desde la izquierda corriendo los bits hacia la derecha:")
print(f"{bin(x)} >> {z} --> {bin(x>>z)}")
print('')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OPERADORES DE ASIGNACIÓN
print("\nOPERADORES DE ASIGNACIÓN\n")

# Los operadores de asignación se utilizan para asignar variables a variables.
x, y = 10, 2
print("uso de operadores de asignación en python")
print(f"operador (+=): x+=y es lo mismo que x=x+y")
print(f"x = {x}, y = {y}:")
x += y
print(f"x+=y: {x}")
print(f"operador (-=): x-=y es lo mismo que x=x-y")
print(f"x = {x}, y = {y}:")
x -= y
print(f"x+=y: {x}")
print(f"operador (*=): x*=y es lo mismo que x=x*y")
print(f"x = {x}, y = {y}:")
x *= y
print(f"x*=y: {x}")
print(f"operador (/=): x/=y es lo mismo que x=x/y")
print(f"x = {x}, y = {y}:")
x /= y
print(f"x/=y: {x}")
print(f"operador (%=): x%=y es lo mismo que x=x%y")
print(f"x = {x}, y = {y}:")
x %= y
print(f"x+=y: {x}")
x= 10
print(f"operador (**=): x**=y es lo mismo que x=x**y")
print(f"x = {x}, y = {y}:")
x **= y
print(f"x**=y: {x}")
print(f"operador (//=): x/=y es lo mismo que x=//y")
print(f"x = {x}, y = {y}:")
x //= y
print(f"x//=y: {x}")
print('')
