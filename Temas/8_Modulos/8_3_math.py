# ------------------------------------------------------------------------------------------------
# Tema 8_3: Matemáticas en Python
# ------------------------------------------------------------------------------------------------

# Python tiene un conjunto de funciones matemáticas integradas, incluido un módulo matemático extenso, 
# que permite realizar tareas matemáticas con números.

# ------------------------------------------------------------------------------------------------
# FUNCIONES MATEMÁTICAS INTEGRADAS

# Las funciones min() y max() se pueden usar para encontrar el valor más bajo o más alto en un iterable:
print("\nFUNCIONES MATEMÁTICAS INTEGRADAS\n")
iter1 = (5, 10, 25)

print("Las funciones min() y max() se pueden usar para encontrar el valor más bajo o más alto en un iterable")
print(f"El máximo del iterable {iter1} es: {max(iter1)}")
print(f"El mínimo del iterable {iter1} es: {min(iter1)}")
print('')

# La función abs() devuelve el valor absoluto (positivo) del número especificado: 
num1 = -7.25
x = abs(num1)
print("La función abs() devuelve el valor absoluto (positivo) del número especificado:")
print(f"El valor absoluto del número {num1} es: {x}")
print('')

# La función pow(x, y) devuelve el valor de x elevado a y
x = pow(4, 3)  # Es equivalente a 4 elevado a la 3
print("La función pow(x, y) devuelve el valor de x elevado a y")
print(f"4 elevado a la 3 es igual a: {x}")
print('')

# ------------------------------------------------------------------------------------------------
# MÓDULO MATEMÁTICO EN PYTHON
# Python también tiene un módulo incorporado llamado math, que amplía la lista de funciones matemáticas.
print("\nMÓDULO MATEMÁTICO EN PYTHON\n")
import math

# El método math.sqrt(), por ejemplo, devuelve la raíz cuadrada de un número.
num1 = 64
x = math.sqrt(num1)
print("El método math.sqrt(), por ejemplo, devuelve la raíz cuadrada de un número.")
print(f"La raíz cuadrada del número {num1} es: {x}")
print('')

# El método math.ceil() redondea un número hacia arriba hasta su entero más cercano y devuelve su resultado:
num1 = 1.4
x = math.ceil(num1)
print("El método math.ceil() redondea un número hacia arriba hasta su entero más cercano")
print(f"Redondeando el número {num1} hacia arriba: {x}")
print('')

# El método math.floor() redondea un número hacia abajo hasta su entero más cercano y devuelve el resultado.
y = math.floor(num1)
print("El método math.floor() redondea un número hacia abajo hasta su entero más cercano")
print(f"Redondeando el número {num1} hacia abajo: {y}")
print('')

# Métodos adicionales del módulo math

# El método math.log() devuelve el logaritmo natural de un número.
num2 = 100
log_value = math.log(num2)
print("El método math.log() devuelve el logaritmo natural de un número.")
print(f"El logaritmo natural del número {num2} es: {log_value}")
print('')

# El método math.sin() devuelve el seno de un ángulo (en radianes).
angle = math.pi / 2  # 90 grados
sin_value = math.sin(angle)
print("El método math.sin() devuelve el seno de un ángulo (en radianes).")
print(f"El seno de {angle} radianes es: {sin_value}")
print('')

# El método math.cos() devuelve el coseno de un ángulo (en radianes).
cos_value = math.cos(angle)
print("El método math.cos() devuelve el coseno de un ángulo (en radianes).")
print(f"El coseno de {angle} radianes es: {cos_value}")
print('')

# El método math.tan() devuelve la tangente de un ángulo (en radianes).
tan_value = math.tan(angle)
print("El método math.tan() devuelve la tangente de un ángulo (en radianes).")
print(f"La tangente de {angle} radianes es: {tan_value}")
print('')

# Constantes del módulo math:
pi = math.pi
euler = math.e
inf = math.inf
tau = math.tau
nan = math.nan
print("El módulo math contiene una serie de constantes importantes usadas en operaciones matemáticas:")
print(f"Número pi en el módulo math: {pi}")
print(f"Número euler en el módulo math: {euler}")
print(f"Número inf en el módulo math: {inf}")
print(f"Número tau en el módulo math: {tau}")
print(f"Número nan en el módulo math: {nan}")
print('')
