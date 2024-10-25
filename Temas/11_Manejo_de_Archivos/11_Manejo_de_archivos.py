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
# MANEJANDO ARCHIVOS CON 'with'
# Usar 'with' para manejar archivos es una buena práctica, ya que asegura que el archivo se cierre automáticamente al final del bloque,
# incluso si ocurre un error. Esto es especialmente útil para evitar fugas de recursos.

print("Ejemplo 9: Usando 'with' para manejar archivos de forma segura")
with open("demofile.txt", "r") as f:
    contenido = f.read()  # Lee todo el contenido del archivo
    print("Contenido del archivo leído con 'with':")
    print(contenido)
print("El archivo se cierra automáticamente al salir del bloque 'with'.")
print('')

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# MANEJANDO ARCHIVOS Y DIRECTORIOS CON 'os'
# El módulo 'os' proporciona una forma de interactuar con el sistema operativo y realizar operaciones relacionadas con archivos y directorios.

import os

# LISTANDO ARCHIVOS EN UN DIRECTORIO
# Para listar todos los archivos y carpetas en un directorio, se utiliza os.listdir().
print("Ejemplo 10: Listando archivos y carpetas en el directorio actual:")
archivos_y_carpetas = os.listdir()  # Lista los archivos y carpetas en el directorio actual
print(archivos_y_carpetas)
print('')

# CAMBIANDO EL DIRECTORIO DE TRABAJO
# Para cambiar el directorio de trabajo actual, se utiliza os.chdir().
directorio_original = os.getcwd()  # Guarda el directorio actual para volver más tarde
print("Ejemplo 11: Cambiando el directorio de trabajo:")
os.chdir('myfolder')  # Cambia el directorio de trabajo a 'myfolder'
print(f"Nuevo directorio de trabajo: {os.getcwd()}")
print('')

# CREANDO UN NUEVO DIRECTORIO
# Para crear un nuevo directorio, se utiliza os.mkdir().
print("Ejemplo 12: Creando un nuevo directorio:")
if not os.path.exists("nuevo_directorio"):
    os.mkdir("nuevo_directorio")
    print("Directorio 'nuevo_directorio' creado.")
else:
    print("El directorio 'nuevo_directorio' ya existe.")
print('')

# VERIFICANDO LA EXISTENCIA DE UN ARCHIVO
# Para verificar si un archivo existe, se puede usar os.path.exists().
print("Ejemplo 13: Verificando la existencia de un archivo:")
archivo = "demofile5.txt"
if os.path.exists(archivo):
    print(f"El archivo '{archivo}' existe.")
else:
    print(f"El archivo '{archivo}' no existe.")
print('')

# OBTENIENDO INFORMACIÓN SOBRE UN ARCHIVO
# Para obtener información sobre un archivo, se utiliza os.stat().
print("Ejemplo 14: Obteniendo información sobre un archivo:")
if os.path.exists(archivo):
    info_archivo = os.stat(archivo)
    print(f"Tamaño del archivo '{archivo}': {info_archivo.st_size} bytes")
    print(f"Última modificación: {info_archivo.st_mtime}")
print('')

# CAMBIANDO EL NOMBRE DE UN ARCHIVO
# Para renombrar un archivo, se utiliza os.rename().
print("Ejemplo 15: Cambiando el nombre de un archivo:")
nuevo_nombre = "nuevo_demofile.txt"
if os.path.exists(archivo):
    os.rename(archivo, nuevo_nombre)
    print(f"Archivo renombrado a '{nuevo_nombre}'.")
else:
    print(f"El archivo '{archivo}' no existe para renombrar.")
print('')

# ELIMINANDO UN DIRECTORIO VACÍO
# Para eliminar un directorio vacío, se utiliza os.rmdir().
print("Ejemplo 16: Eliminando un directorio vacío:")
if os.path.exists("nuevo_directorio"):
    os.rmdir("nuevo_directorio")
    print("Directorio 'nuevo_directorio' eliminado.")
else:
    print("El directorio 'nuevo_directorio' no existe.")
print('')

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# CAMBIANDO DE DIRECTORIO MEDIANTE JOIN
# También es posible cambiarse de directorio definiendo la ruta con el método join() del módulo os.
print("Ejemplo 17: Navegando entre carpetas utilizando os.path.join()")
# Obtiene el directorio actual
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# se define una carpeta nueva
carpeta_nueva = "myfolder"
# se une el directorio actual con la nueva carpeta utilizando os.path.join()
# Esto crea una ruta completa válida para el sistema operativo
ruta_completa = os.path.join(directorio_actual, carpeta_nueva)

# se cambia al nuevo directorio utilizando la ruta completa
os.chdir(ruta_completa)
print(f"Cambiado al directorio: {os.getcwd()}")  # Muestra el nuevo directorio de trabajo

# se regresa al directorio original
os.chdir(directorio_actual)
print(f"Regresando al directorio original: {os.getcwd()}")  # Verifica que se regreso al directorio original
print('')

# CREANDO UNA RUTA DE ACCESO ABSOLUTA
# A veces es útil obtener la ruta completa de un archivo o directorio
print("Ejemplo 18: Creando una ruta de acceso absoluta:")
nombre_archivo = "demofile.txt"
# os.path.join() permite combinar el directorio actual con el nombre del archivo y obtener la ruta completa
ruta_archivo = os.path.join(directorio_actual, nombre_archivo)
print(f"Ruta completa del archivo: {ruta_archivo}")
print('')

# NAVEGANDO HACIA EL DIRECTORIO PADRE CON OS
# Si se necesita volver al directorio superior o "padre", es posible hacerlo usando '..'
print("Ejemplo 19: Navegando hacia el directorio padre:")
# se cambia al directorio 'myfolder' si existe
carpeta_nueva = "myfolder"
ruta_completa = os.path.join(directorio_actual, carpeta_nueva)

if os.path.exists(ruta_completa):
    os.chdir(ruta_completa)  # Cambia al directorio especificado
    print(f"Cambiado al directorio: {os.getcwd()}")  # Verifica que se esta en el nuevo directorio
else:
    print(f"La carpeta {carpeta_nueva} no existe en {directorio_actual}.")

# vuelve al directorio padre utilizando ".."
os.chdir('..')  # se Utiliza '..' para subir un nivel en la estructura de directorios.
print(f"Regresando al directorio padre: {os.getcwd()}")  # Confirma que se esta en el directorio superior
print('')

# NAVEGANDO A TRAVÉS DE RUTAS RELATIVAS CON OS
# Es posible navegar entre directorios utilizando rutas relativas, lo que permite subir y bajar niveles en la estructura de directorios.
print("Ejemplo 20: Navegando hacia un nuevo directorio usando rutas relativas:")

# Suponiendo que se encuentra en el directorio 'myfolder' y se quiere ir a 'nuevo_directorio' que está en el mismo nivel que 'myfolder'
# Primero, se cambia a 'myfolder' si existe
carpeta_nueva = "myfolder"
ruta_completa = os.path.join(directorio_actual, carpeta_nueva)

if os.path.exists(ruta_completa):
    os.chdir(ruta_completa)  # Cambia al directorio 'myfolder'
    print(f"Cambiado al directorio: {os.getcwd()}")  # Verifica que se encuentra en 'myfolder'
else:
    print(f"La carpeta {carpeta_nueva} no existe en {directorio_actual}.")

# suponiendo que hay otro directorio en el nivel superior llamado 'nuevo_directorio'
nuevo_directorio = "newfolder"

# se navega al directorio padre (usando '..') y luego al nuevo directorio
os.chdir(f'../{nuevo_directorio}')  # Usa '../' para subir un nivel y luego ir a 'newfolder'
print(f"Navegando a: {os.getcwd()}")  # se confirma que se encuentra en 'newfolder'


"""# --------------------------------------------------------------------------------------------------------------------------------------------------------
# ELIMINANDO UN ARCHIVO EN PYTHON
# Para eliminar un archivo, se debe ejecutar la función os.remove() del módulo os.
# Sin embargo, para evitar obtener un error, se debe verificar si el archivo existe antes de intentar eliminarlo:
if os.path.exists("myfile.txt"):
    print("Ejemplo 21: Eliminando el archivo myfile.txt")
    os.remove("myfile.txt")
else:
    print("El archivo no existe.")

# Para eliminar una carpeta entera, se debe utilizar el método os.rmdir():

import os
os.rmdir("myfolder")

"""