# ------------------------------------------------------------------------------------------------
# Tema 8_2: Fechas en Python
# ------------------------------------------------------------------------------------------------

# Fechas en Python
# Una fecha en Python no es un tipo de datos en sí misma, pero es posible importar un módulo llamado datetime 
# para trabajar con fechas como objetos de fecha:
import datetime

# ------------------------------------------------------------------------------------------------
# USO DEL MÓDULO DATETIME EN PYTHON
print("\nMÓDULO DATETIME EN PYTHON\n")
print("El módulo datetime permite trabajar con fechas como objetos de fecha en Python.")
x = datetime.datetime.now()
print("Tipo de objeto datetime: ", type(x))
print(f"Obteniendo la fecha y hora actual del sistema operativo donde se ejecuta el programa: {x}")
print('')

# El módulo datetime tiene muchos métodos para devolver información sobre el objeto de fecha:
print("\nMÉTODOS DEL OBJETO DATETIME\n")
print("El objeto datetime tiene muchos métodos para devolver información sobre el objeto de fecha.")
print("El año actual es: ", x.year)
print("El día de la semana actual es: ", x.strftime("%A"))
print('')

# CREACIÓN DE OBJETOS DE TIPO FECHA
# Para crear una fecha, se debe utilizar la clase datetime() (constructor) del módulo datetime.
# La clase datetime() requiere tres parámetros para crear una fecha: año, mes, día.
# Nota:
#   La clase datetime() también toma parámetros para la hora y la zona horaria (hora, minuto, segundo, microsegundo, zona horaria), 
#   pero son opcionales y tienen un valor predeterminado de 0 (Ninguno para la zona horaria).
print("\nCREACIÓN DE OBJETOS DE TIPO FECHA\n")
print("Para crear una fecha, se debe utilizar el constructor del módulo datetime.")
y = datetime.datetime(2020, 5, 17)
print(f"Accediendo al objeto de tipo fecha construido a partir del módulo datetime: {y}")
print('')

# El método strftime()
# El objeto datetime tiene un método para formatear objetos de fecha en cadenas legibles.
# El método se llama strftime() y toma un parámetro, format, para especificar el formato de la cadena devuelta:
z = datetime.datetime.now()

print("\nMÉTODO STRFTIME()\n")
print(f"El objeto datetime tiene un método para formatear objetos de fecha en cadenas legibles llamado strftime().")
month = z.strftime("%B")
print(f'El mes actual es: {month} y es del tipo {type(month)}')
print('')

# A continuación se listan todos los códigos de formato para trabajar con los objetos de tipo datetime:
print("\nFORMATOS PARA LOS OBJETOS DE TIPO DATETIME\n")
print(f'Día de la semana actual (versión corta): {z.strftime("%a")}')
print(f'Día de la semana actual (versión completa): {z.strftime("%A")}')
print(f'Día de la semana actual (como un número, donde 0 representa el domingo): {z.strftime("%w")}')
print(f'Día del mes actual: {z.strftime("%d")}')
print(f'Mes actual (versión corta): {z.strftime("%b")}')
print(f'Mes actual (versión completa): {z.strftime("%B")}')
print(f'Mes actual (como un número del 1 al 12): {z.strftime("%m")}')
print(f'Año actual (versión corta): {z.strftime("%y")}')
print(f'Año actual (versión completa): {z.strftime("%Y")}')
print(f'Hora actual (formato de 24 horas): {z.strftime("%H")}')
print(f'Hora actual (formato de 12 horas): {z.strftime("%I")}')
print(f'Hora actual (AM/PM): {z.strftime("%p")}')
print(f'Minuto actual: {z.strftime("%M")}')
print(f'Segundo actual: {z.strftime("%S")}')
print(f'Microsegundo actual: {z.strftime("%f")}')
print(f'Zona horaria actual: {z.strftime("%Z")}')
print(f'UTC offset: {z.strftime("%z")}')
print('')

# Sumando o restando días a una fecha con timedelta
# En Python, se puede utilizar timedelta del módulo datetime para sumar o restar días, meses o años a una fecha.
print("\nSUMANDO O RESTANDO DÍAS A UNA FECHA CON TIMDELTA\n")
from datetime import timedelta

# Sumar 10 días a la fecha actual
future_date = z + timedelta(days=10)
print(f'Fecha actual: {z}')
print(f'Fecha después de sumar 10 días: {future_date}')

# Restar 5 días a la fecha actual
past_date = z - timedelta(days=5)
print(f'Fecha después de restar 5 días: {past_date}')
print('')
