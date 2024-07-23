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

