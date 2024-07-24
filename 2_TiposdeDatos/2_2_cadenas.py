# Tema 2: Tipos de datos en python
# 2.2 cadenas de texto

# Las cadenas en Python se pueden escribir entre comillas simples o dobles
print("Las cadenas se pueden escribir entre comillas simples o dobles: ")
str1 = "hola"
str2 = 'python'
print(f"{str1} desde {str2}")
print('')

# Es posible asignar una cadena de texto de varias líneas a una variable utilizando tres comillas
# Nota: en el resultado, los saltos de línea se insertan en la misma posición que en el código
print("Es posible asignar una cadena de texto de varias líneas a una variable: ")
str3 = """hola esta es una cadena de texto de multples lineas 
escrita mediante la sintaxis de tres comillas 
desde python
"""
print(str3)
print('')

# las cadenas en Python son matrices de bytes que representan caracteres Unicode.
# Por lo tanto, se pueden utilizar corchetes para acceder a los elementos de la cadena de texto.
# Nota: Python no tiene un tipo de datos de carácter, un solo carácter es simplemente una cadena con una longitud de 1.
print("para acceder a los caracteres de una cadena de texto se debe utilizar corchetes []: ")
a = "Hello, World!"
a1 = a[1]
a2 = a[2:5] # obtiene los acracteres de la posición 2 a la posición 5 (no incluye el 5)
a3 = a[:5]  # si se omite el índice inicial, el rango comenzará en el primer carácter (no incluye el 5)
a4 = a[6:]  # al omitir el índice final , el rango irá hasta el final (incluye el 6)
a5 = a[-2]  # obtiene el penultimo caracter 
print(f"el segundo caracter de la cadena de texto \"{a}\" es: {a1}")
print(f"los caracteres 3 y 4 de la cadena de texto \"{a}\" son: {a2}")
print(f"los primeros 4 caracteres de la cadena de texto \"{a}\" son: {a3}")
print(f"los caracteres desde la posicion 6 hasta el final, de la cadena de texto \"{a}\" son: {a4}")
print(f"el penultimo caracter de la cadena de texto \"{a}\", obtenido mediante indexación negativa es: {a5}")
print('')

# Para obtener la longitud de una cadena de texto, se utiliza la funcion len().
print("El método len() se utiliza para obtener la longitud de una cadena de texto:")
a = "Hello, World!"
print(f"la longitud de la cadena es {len(a)}")
print('')

# Para verificar si un elemento se encuentra dentro de una cadena de texto, se utiliza la palabra clave in
print("Verificando si un elemento se encuentra dentro de una cadena de texto mediante la palabra clave in")
word = 'free'
txt = "The best things in life are free!"
print(f" se verifica si la palabra: {word} esta presente en el texto: \n \"{txt}\"")
print(f"resultado de la verificacion: {word in txt}")
print('')

# Para combinar dos cadenas de texto se puede utilizar el operador + o la funcion format.
print("cocatenando dos o mas cadenas de texto")
str1 = 'Hello'
str2 = 'World'
str3 = str1 + str2  # cocatenacion simple
aux1 = "My name is Edward, and I am {}"
str4 = aux1.format(25) # cocatenando un string con un entero
print(f"cocatenacion simple con el operador +: {str3}")
print(f"cocatenacion multiple utilizando el metodo format: {str4}")
print('')

# Python tiene un conjunto de metodos que operan sobre las cadenas de texto
# Nota: Todos los métodos de cadena devuelven nuevos valores. No cambian la cadena original.
print("Metodos de python sobre cadenas de texto")
a = " Hello, World!"
m1 = a.upper()  # convierte una cadena de texto a mayusculas
m2 = a.lower()  # convierte una cadena de texto en minusculas
m3 = a.strip()  # elimina espacios en blanco antes o despues de la cadena de texto
m4 = a.replace('Hello', 'Good bye') # reemplaza una cadena de texto con otra
m5 = a.split(",")   # devuelve una lista donde el texto entre el separador especificado se convierte en los elementos de la lista.
m6 = a.count("l")   # devuelve el numero de veces que un valor especifico se repite en la cadena de texto
m7 = a.find("wor")  # busca en la cadena un valor específico y devuelve la posición donde se encontró
m8 = a.index("d")   # Busca en la cadena un valor específico y devuelve la posición donde se encontró
quantity, itemno, price = 3, 567, 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
m9 =  myorder.format(quantity, itemno, price) # permite cocatenar cadenas de texto con otro tipo de variables. El metodo format recibe un numero de argumentos ilimitados, los cuales se reemplazan en el orde establecido
m10 = "#".join(["hello", "my", "name", "is", "edward"])  # Une todos los elementos de un iterable en una cadena de texto, usando el caracter especificado como separador
print(f"método upper:   {m1}")
print(f"método lower:   {m2}")
print(f"método strip:   {m3}")
print(f"método replace: {m4}")
print(f"método split:   {m5}")
print(f"método count:   {m6}")
print(f"método find:    {m7}")
print(f"método index:   {m8}")
print(f"método format:  {m9}")
print(f"método join:    {m10}")
print('')
