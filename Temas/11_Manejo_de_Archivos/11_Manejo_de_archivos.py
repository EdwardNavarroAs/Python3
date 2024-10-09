# Python tiene varias funciones para crear, leer, actualizar y eliminar archivos.

# La función clave para trabajar con archivos en Python es la función open().
# open() toma dos parámetros: nombre de archivo y modo de apertura.
# Hay cuatro modos básicos para abrir un archivo:

# "r" - Leer (Read) - Valor predeterminado. Abre un archivo para lectura. Da un error si el archivo no existe.
# "a" - Anexar (Append) - Abre un archivo para anexar contenido. Crea el archivo si no existe.
# "w" - Escribir (Write) - Abre un archivo para escribir (sobreescribe si ya existe). Crea el archivo si no existe.
# "x" - Crear (Create) - Crea el archivo especificado. Da un error si el archivo ya existe.

# Además, es posible especificar si el archivo debe manejarse en modo binario o de texto:

# "t" - Texto (Text) - Valor predeterminado. Modo texto (para archivos de texto).
# "b" - Binario (Binary) - Modo binario (para archivos como imágenes o videos).

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# ABRIENDO UN ARCHIVO EN PYTHON
# Supongamos que tenemos el archivo "demofile.txt", ubicado en la misma carpeta donde está este script de Python.
# Para abrir el archivo, usamos la función open().
# La función open() devuelve un objeto de archivo, que tiene un método read() para leer el contenido.

f = open("demofile.txt")
print("Para abrir un archivo desde Python se utiliza la función open(). Una vez abierto, se puede leer su contenido con el método read().")
print("Ejemplo 1: Leyendo el contenido de un archivo de texto desde Python:")
print(f.read())
print('')

# Si el archivo se encuentra en una ubicación diferente, se debe especificar la ruta completa del archivo:
print("Si el archivo se encuentra en una ubicación diferente, se debe especificar la ruta del archivo.")
print("Ejemplo 2: Especificando la ruta de un archivo para ser leído:")
f = open(r"myfile\demofile2.txt", "r") 
print(f.read())
print('')

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# LEYENDO UN ARCHIVO EN PYTHON
# De manera predeterminada, el método read() devuelve todo el contenido del archivo.
# Sin embargo, es posible especificar cuántos caracteres se quieren leer:

print("De manera predeterminada, el método read() devuelve todo el contenido del archivo.")
print("Sin embargo, es posible leer solo una cantidad específica de caracteres.")
print("Ejemplo 3: Leyendo solo los primeros 5 caracteres de un archivo de texto:")
f = open("demofile.txt", "r")
print(f.read(5))  # Lee los primeros 5 caracteres del archivo
print('')

# También es posible devolver una línea completa de un archivo de texto utilizando el método readline():
print("El método readline() permite leer una línea completa de un archivo de texto.")
print("Ejemplo 4: Leyendo una línea de un archivo de texto:")
f = open("demofile.txt", "r")
print(f.readline())  # Lee la primera línea del archivo
print(f.readline())  # Lee la segunda línea del archivo
print('')

# Al recorrer las líneas de un archivo con un bucle, podemos leerlo completo línea por línea:
print("Ejemplo 5: Recorriendo un archivo de texto línea por línea:")
f = open("demofile.txt", "r")
for x in f:
    print(x, end='')  # Se añade 'end' para evitar una nueva línea adicional, ya que cada línea incluye su propio salto de línea
print('')

# Es una buena práctica cerrar siempre el archivo una vez que se haya utilizado para liberar recursos del sistema.
print("Una vez que se ha terminado de utilizar el archivo, es importante cerrarlo utilizando el método close().")
f = open("demofile.txt", "r")
print(f.readline())
f.close()  # Cerramos el archivo
print('')
