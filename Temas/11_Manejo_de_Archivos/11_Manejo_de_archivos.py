# Python tiene varias funciones para crear, leer, actualizar y eliminar archivos.

# La función clave para trabajar con archivos en Python es la función open().
# open() toma dos parámetros: nombre de archivo y modo de apertura.
# Hay cuatro modos básicos para abrir un archivo:

# "r" - Leer (Read) - Valor predeterminado. Abre un archivo para lectura. Da un error si el archivo no existe.
# "a" - Anexar (Append) - Abre un archivo para anexar contenido. Crea el archivo si no existe.
# "w" - Escribir (Write) - Abre un archivo para escribir (sobrescribe si ya existe). Crea el archivo si no existe.
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
f.close()  # Asegúrate de cerrar el archivo después de usarlo

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
f.close()  # Cierra el archivo

# También es posible devolver una línea completa de un archivo de texto utilizando el método readline():
print("El método readline() permite leer una línea completa de un archivo de texto.")
print("Ejemplo 4: Leyendo una línea de un archivo de texto:")
f = open("demofile.txt", "r")
print(f.readline())  # Lee la primera línea del archivo
print(f.readline())  # Lee la segunda línea del archivo
print('')
f.close()  # Cierra el archivo

# Al recorrer las líneas de un archivo con un bucle, podemos leerlo completo línea por línea:
print("Ejemplo 5: Recorriendo un archivo de texto línea por línea:")
f = open("demofile.txt", "r")
for x in f:
    print(x, end='')  # Se añade 'end' para evitar una nueva línea adicional
print('')
f.close()  # Cierra el archivo

# Es una buena práctica cerrar siempre el archivo una vez que se haya utilizado para liberar recursos del sistema.
print("Una vez que se ha terminado de utilizar el archivo, es importante cerrarlo utilizando el método close().")
f = open("demofile.txt", "r")
print(f.readline())
f.close()  
print('')


# ESCRIBIENDO EN UN ARCHIVO EN PYTHON
# Para escribir en un archivo existente, se debe agregar un parámetro a la función open():
# "a" - Anexar - Se agregará al final del archivo.
# "w" - Escritura - Sobrescribirá cualquier contenido existente (si no existe, lo crea).

# Luego, es posible agregarle contenido al archivo mediante el método write().
print("Para escribir en un archivo existente, se debe agregar el parámetro 'a' ó 'w' a la función open() y luego utilizar el método write().")
print("Ejemplo 6: Abriendo un archivo y agregándole contenido al final.")
f1 = open("demofile.txt", "r") 
print(f"\nContenido original:")
print(f1.read())
f1.close()  # Cierra el archivo original

f = open("demofile.txt", "a")
f.write("Se ha agregado contenido nuevo!")
f.close()  # Cierra el archivo después de escribir

f = open("demofile.txt", "r")
print("\nContenido modificado:")
print(f.read())
print('')
f.close()  # Cierra el archivo

print("Ejemplo 7: Abriendo un archivo y sobrescribiendo su contenido en su totalidad.")
f = open("demofile3.txt", "w") 
f.write("Se ha sobreescrito completamente el contenido de este archivo. Saludos!")
f.close()  # Cierra el archivo después de escribir

f = open("demofile3.txt", "r")
print("Contenido del archivo sobrescrito:")
print(f.read())
print('')
f.close()  # Cierra el archivo

# Para crear un archivo nuevo con la función open() se debe utilizar el parámetro 'x'.
print("Para crear un archivo nuevo, se debe agregar el parámetro 'x' a la función open().")
print("Ejemplo 8: Creando un archivo nuevo vacío.")
try:
    f = open("myfile.txt", "x")  # Intenta crear un nuevo archivo
    f.close()  # Cierra el archivo después de crearlo
    print("Archivo 'myfile.txt' creado exitosamente.")
    
except FileExistsError:
    print("Error: El archivo 'myfile.txt' ya existe.")
finally:
    print('')

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# ELIMINANDO UN ARCHIVO EN PYTHON
# Para eliminar un archivo, se debe importar el módulo OS y ejecutar la función os.remove().
# Sin embargo, para evitar obtener un error, se debe verificar si el archivo existe antes de intentar eliminarlo:
import os

if os.path.exists("myfile.txt"):
    print("Ejemplo 9: Eliminando el archivo myfile.txt")
    os.remove("myfile.txt")
else:
    print("El archivo no existe.")

# Para eliminar una carpeta entera, se debe utilizar el método os.rmdir():
"""
import os
os.rmdir("myfolder")
"""

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# MANEJANDO ARCHIVOS CON 'with'
# Usar 'with' para manejar archivos es una buena práctica, ya que asegura que el archivo se cierre automáticamente al final del bloque,
# incluso si ocurre un error. Esto es especialmente útil para evitar fugas de recursos.

print("Ejemplo 10: Usando 'with' para manejar archivos de forma segura")
with open("demofile.txt", "r") as f:
    contenido = f.read()  # Lee todo el contenido del archivo
    print("Contenido del archivo leído con 'with':")
    print(contenido)
print("El archivo se cierra automáticamente al salir del bloque 'with'.")
print('')
