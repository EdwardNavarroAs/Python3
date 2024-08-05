import asyncio
# Tema 5: funciones en Python

# Una función es un bloque de código que solo se ejecuta cuando se la llama, pudiendo recibir ciertos datos de entrada
# o argumentos para ser procesados dentro de la misma función y pudiendo brindar datos de salida como resultado.

# En Python, una función se define usando la palabra reservada 'def'
print("\nDEFINICIÓN DE UNA FUNCIÓN EN PYTHON\n")
def my_function():
    print("Hola desde una función en Python")

print("Utilizando la sintaxis para llamar una función en Python")
my_function()
print('')

# Argumentos
# La información se puede pasar a funciones como argumentos. Los argumentos se especifican después del nombre de la función,
# dentro del paréntesis. En las funciones es posible agregar tantos argumentos como se deseen, separados por una coma.
# Nota:
# Los términos parámetro y argumento se pueden usar para lo mismo: información que se pasa a una función.
# Desde la perspectiva de una función:
#   - Un parámetro es la variable que figura entre paréntesis en la definición de la función.
#   - Un argumento es el valor que se envía a la función cuando se llama.

# Usando parámetros para definir una función
print("\nUSO DE ARGUMENTOS EN FUNCIONES DE PYTHON\n")
def my_function2(name):
    print(f"Hola {name} desde Python")

print("Utilizando argumentos dentro de una función en Python")
# Usando argumentos al llamar una función
my_function2("Edward")
my_function2("Tobias")
print('')

# Argumentos arbitrarios, *args
# Si no se sabe cuántos argumentos se pasarán a una función, se debe agregar un * antes del nombre del parámetro 
# en la definición de la función. De esta manera, la función recibirá una tupla de argumentos y será posible acceder 
# a los elementos en consecuencia.

# Nota: En la documentación de Python, los argumentos arbitrarios a menudo se abrevian como *args.
print("\nARGUMENTOS ARBITRARIOS EN PYTHON\n")
def my_function3(*args):
    print(f"El tercer elemento de los argumentos dados es: {args[2]}")

print("Agregando una cantidad indefinida de argumentos en una función")
my_function3("Emil", "Tobias", "Linus")
print('')

# En Python, también es posible tener argumentos con la sintaxis clave = valor. De esta forma, no importa en qué 
# orden se envían los argumentos a la función.
print("\nARGUMENTOS CON LA SINTAXIS CLAVE = VALOR EN PYTHON\n")
def my_function4(child3, child2, child1):
    print(f"El más joven de los niños es: {child3}")

print("Agregando argumentos con la sintaxis clave = valor en una función")
my_function4(child1="Emil", child2="Tobias", child3="Linus")
print('')

# Argumentos con la sintaxis clave=valor, **kwargs
# Si no se sabe cuántos argumentos con sintaxis clave = valor se pasarán a una función, se deben agregar dos asteriscos ** antes del nombre del parámetro 
# en la definición de la función. De esta manera, la función recibirá un diccionario de argumentos y será posible acceder 
# a los elementos en consecuencia.

# Nota: En la documentación de Python, los argumentos con sintaxis clave = valor arbitrarios a menudo se abrevian como **kwargs.
print("\nARGUMENTOS ARBITRARIOS CON PALABRA CLAVE EN PYTHON\n")
def my_function4_1(**kwargs):
    print(f"El nombre del segundo niño es: {kwargs['kid2']['name']}")

print("Agregando una cantidad indefinida de argumentos con palabra clave en una función")
my_function4_1(kid1={"name": "Tobias", "age": 8}, kid2={"name": "Emil", "age": 10})
print('')

# Python admite funciones con parámetros con valores por defecto. Cuando se llama a la función sin argumento, 
# la función usa el valor predeterminado.
print("\nPARÁMETROS PREDETERMINADOS EN UNA FUNCIÓN\n")
def my_function5(country="Norway"):
    print(f"I am from {country}")

print("Utilizando el valor por defecto de un parámetro en una función")
my_function5("Colombia")
my_function5()
print('')

# Las funciones en Python pueden recibir cualquier tipo de argumento de datos (cadena, número, lista, diccionario, etc.)
# y será tratado como el mismo tipo de datos dentro de la función.
print("\nLAS FUNCIONES PUEDEN RECIBIR CUALQUIER TIPO DE DATO\n")
def my_function6(food):
    [print(x) for x in food]

fruits = ["apple", "banana", "cherry"]

print("Las funciones en Python pueden recibir cualquier tipo de dato como argumento")
print("Enviando una lista a una función")
my_function6(fruits)
print('')

# Para permitir que una función en Python devuelva un valor, se debe usar la palabra clave return:
print("\nRETORNANDO VALORES EN UNA FUNCIÓN\n")
arg1, arg2 = 5, 3
def my_function7(x):
    return 5 * x

print("Retornando valores en una función")
print(f"El valor que retorna la función para el argumento {arg1} es: {my_function7(arg1)}")
print(f"El valor que retorna la función para el argumento {arg2} es: {my_function7(arg2)}")
print('')

# Las definiciones de funciones en python no pueden estar vacías, 
# pero si por alguna razón se necesita definir una función sin contenido, se debe utilizar la palabra clave pass.
def myfinalfunction():
  pass

# Argumentos únicamente posicionales
# En Python es posible especificar que una función pueda tener SÓLO argumentos posicionales o SÓLO argumentos con sintaxis clave = valor.
# Para especificar que una función solo puede tener argumentos posicionales, se debe agregar / después de los argumentos:
# Nota:
#   - Al agregar / se producirá un error si se intenta enviar un argumento de palabra clave:
print("\nFUNCIONES QUE RECIBEN ÚNICAMENTE ARGUMENTOS POSICIONALES\n")
def my_function8(x, /):
    print(x)

print("Utilizando funciones que únicamente admiten argumentos posicionales")
my_function8(3)
# Esto produciría un error: my_function8(x=3)
print('')

# Argumentos de solo sintaxis clave = valor
# En Python es posible especificar que una función solo puede tener argumentos con sintaxis clave = valor.
# Para especificar que una función solo puede tener argumentos con sintaxis clave = valor, se debe agregar * antes de los argumentos:
print("\nFUNCIONES QUE RECIBEN ÚNICAMENTE ARGUMENTOS CON SINTAXIS CLAVE = VALOR\n")
def my_function9(*, x):
    print(x)

print("Utilizando funciones que únicamente admiten argumentos con sintaxis clave = valor")
my_function9(x=3)
# Esto produciría un error: my_function9(3)
print('')

#En python es posible combinar los dos tipos de argumentos en la misma función.
# Cualquier argumento antes de / es solo posicional, mientras que, cualquier argumento después de * son argumentos con sintaxis clave = valor.
print("\nFUNCIONES QUE RECIBEN ARGUMENTOS POSICIONALES Y CON SINTAXIS CLAVE = VALOR\n")
def my_function10(a, b, /, *, c, d):
    print(a + b + c + d)

print("Utilizando funciones que admiten argumentos posicionales y argumentos con sintaxis clave = valor")
my_function10(5, 6, c = 7, d = 8)
print('')

# Recursividad
# Python también acepta la recursividad de funciones, lo que significa que una función definida puede llamarse a sí misma.

# La recursividad es un concepto matemático y de programación común. Significa que una función se llama a sí misma. 
# Esto tiene la ventaja de que puede recorrer los datos para llegar a un resultado.

# El desarrollador debe tener mucho cuidado con la recursividad, ya que puede ser bastante fácil escribir una función que nunca termina, 
# o una que utiliza cantidades excesivas de memoria o potencia del procesador. Sin embargo, cuando se escribe correctamente, 
# la recursividad puede ser un enfoque de programación muy eficiente y matemáticamente elegante.
# Ejemplo de recursividad: cálculo del factorial
print("\nRECURSIVIDAD EN PYTHON\n")
def factorial(n):
    """Calcula el factorial de un número n de manera recursiva."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Prueba del cálculo del factorial
number = 5
print("uso de la recursividad en python")
print(f"El factorial de {number} es {factorial(number)}")
print('')

# Función Lambda
# Una función lambda es una pequeña función anónima.
# Una función lambda puede tomar cualquier número de argumentos, pero solo puede tener una expresión.
# La expresión se ejecuta y se devuelve el resultado.

# Sintaxis:
#   result = lambda arguments : expression

print("\nFUNCIÓN LAMBDA EN PYTHON\n")
x = lambda a: a + 10
print("Uso de aplicación de la función lambda")
print(x(5))  # Debería imprimir 15
print('')

# Ejemplo 2: función lambda con dos argumentos
y = lambda a, b: a * b
print("Uso de función lambda con dos argumentos")
print(y(5, 3))  # Debería imprimir 15
print('')

# Ejemplo 3:
print("Uso de función lambda con tres argumentos")
z = lambda a, b, c : a + b + c
print(z(5, 6, 2))
print('')

# ¿Por qué utilizar funciones Lambda?
# El poder de lambda se muestra mejor cuando se usa como una función anónima dentro de otra función.
# Digamos que se tiene una definición de función que toma un argumento y ese argumento se multiplica por un número desconocido.

arg = 10

def myfunc(n):
    return lambda a: a * n

print("Uso de la función lambda dentro de otra función")
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(f"El doble del argumento {arg} es: {mydoubler(arg)}")
print(f"El triple del argumento {arg} es: {mytripler(arg)}")
print('')


# Documentación de funciones (Docstrings)
# Las cadenas de documentación de Python (o docstrings) proporcionan una forma conveniente de asociar la documentación 
# con módulos, funciones, clases y métodos de Python. Se especifican en el código fuente y se utilizan, como un comentario,
# para documentar un segmento específico de código. A diferencia de los comentarios convencionales, el docstring debe describir 
# lo que hace la función, no cómo lo hace.

# Las cadenas de documentación de estilo Google siguen un formato específico inspirado en la guía de estilo de documentación de Google. 
# Ofrecen una forma estructurada de documentar el código Python, incluidos parámetros, valores de retorno y descripciones.
print("\nDOCUMENTACIÓN DE FUNCIONES (DOCSTRINGS)\n")

def documented_function(a, b):
    """
    Esta es una función de ejemplo con documentación (docstring) en Python basada en el estilo de Google.
    
    Args:
        a (int): El primer número.
        b (int): El segundo número.
 
    Returns:
        int: El producto de a y b.
    """
    return a * b

print(documented_function.__doc__)
print('')

# Anotaciones de Tipo (Type Hints)
# Las anotaciones de tipo en Python proporcionan una forma de indicar los tipos de los parámetros de una función 
# y el tipo de retorno esperado. Esto puede ayudar a mejorar la legibilidad del código y facilitar la detección de errores 
# durante el desarrollo. Sin emabargo, las anotaciones de tipo no afectan la ejecución del código, ya que son solo sugerencias.
print("\nANOTACIONES DE TIPO (TYPE HINTS)\n")

def function_with_types(param1: int, param2: str) -> bool:
    """
    Esta función demuestra el uso de anotaciones de tipo en Python.
    
    Args:
        param1 (int): Un número entero.
        param2 (str): Una cadena de texto.
    
    Returns:
        bool: Verdadero si los tipos son correctos.
    """
    print(f"param1: {param1}, param2: {param2}")
    return True

function_with_types(5, "test")
print('')

# Decoradores (Decorators)
# Un decorador en Python es una función que recibe otra función como argumento y extiende o modifica su comportamiento 
# sin cambiar su código. Los decoradores son útiles para añadir funcionalidades de forma modular y reutilizable, 
# como la autenticación, el registro de eventos y la gestión de transacciones.

print("\nFUNCIONES DECORADORAS (DECORATORS)\n")

def log_decorator(func):
    """
    Este es un decorador que imprime mensajes antes y después de ejecutar una función.
    
    Args:
        func (function): La función que va a ser decorada.
    
    Returns:
        function: La función decorada con comportamiento adicional.
    """
    # Usando *args y **kwargs en el decorador log_decorator, este puede manejar funciones con diferentes tipos y cantidades de argumentos, 
    # haciendo que el decorador sea más flexible y reutilizable.
    def wrapper(*args, **kwargs):
        print(f"Llamando a la función {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Terminada la llamada a la función {func.__name__}")
        return result
    return wrapper

@log_decorator
def say_hello(name):
    """
    Imprime un saludo a la persona con el nombre proporcionado.
    
    Args:
        name (str): El nombre de la persona a saludar.
    """
    print(f"Hola, {name}!")

@log_decorator
def add(a, b):
    """
    Suma dos números.
    
    Args:
        a (int): El primer número.
        b (int): El segundo número.
    
    Returns:
        int: La suma de a y b.
    """
    return a + b

# Llamando a la función decorada say_hello
say_hello("Mundo")
print('')
# Llamando a la función decorada add
print(f"Resultado de la suma: {add(3, 5)}")
print('')

# Funciones Anidadas (Nested Functions)
# Las funciones anidadas en Python son funciones definidas dentro de otras funciones. Las funciones internas pueden acceder 
# a las variables locales de la función externa, lo que permite encapsular funcionalidades y crear un ámbito cerrado.

print("\nFUNCIONES ANIDADAS (NESTED FUNCTIONS)\n")

def outer_function(text):
    """
    Esta función externa contiene una función interna que imprime un texto.
    
    Args:
        text (str): El texto a imprimir.
    """
    def inner_function():
        print(text)
    inner_function()

outer_function("Hola desde una función anidada")
print('')

# Clausuras (Closures)
# Una clausura en Python es una función interna que recuerda el estado de las variables en su ámbito externo 
# incluso después de que el ámbito externo haya finalizado. Las clausuras permiten que las funciones retengan datos 
# y sean utilizadas como funciones de orden superior.
print("\nCLAUSURAS (CLOSURES)\n")

def make_multiplier(multiplier):
    """
    Esta función externa devuelve una función interna que multiplica su argumento por un multiplicador dado.
    
    Args:
        multiplier (int): El valor por el cual se multiplicará el argumento de la función interna.
    
    Returns:
        function: Una función que multiplica su argumento por el multiplicador.
    """
    def multiplier_function(number):
        """
        Esta función interna multiplica el número dado por el multiplicador recordado.
        
        Args:
            number (int): El número a multiplicar.
        
        Returns:
            int: El resultado de la multiplicación.
        """
        return number * multiplier
    
    return multiplier_function

# Crear una instancia de la función interna con un multiplicador específico
double = make_multiplier(2)
# Llamar a la función interna con un número específico
print(f"El doble de 5 es: {double(5)}")
print('')

# Crear otra instancia de la función interna con un multiplicador diferente
triple = make_multiplier(3)
# Llamar a la función interna con otro número
print(f"El triple de 5 es: {triple(5)}")
print('')


import asyncio

# Funciones Asincrónicas (Async/Await)
# Las funciones asincrónicas permiten que el código se ejecute de manera concurrente sin bloquear el hilo principal del programa.
# Esto es especialmente útil para operaciones de entrada/salida (I/O) como la lectura de archivos, el acceso a bases de datos 
# o la comunicación a través de la red.

print("\nFUNCIONES ASINCRÓNICAS (ASYNC/AWAIT)\n")

async def fetch_data():
    """
    Simula la obtención de datos de una fuente externa con una espera asincrónica.
    
    Returns:
        str: Mensaje indicando que los datos fueron obtenidos.
    """
    print("Iniciando la obtención de datos...")
    await asyncio.sleep(2)  # Simula una operación I/O que toma 2 segundos
    print("Datos obtenidos.")
    return "Datos"

async def process_data():
    """
    Simula el procesamiento de datos con una espera asincrónica.
    
    Returns:
        str: Mensaje indicando que los datos fueron procesados.
    """
    print("Iniciando el procesamiento de datos...")
    await asyncio.sleep(1)  # Simula una operación de procesamiento que toma 1 segundo
    print("Datos procesados.")
    return "Procesamiento completo"

async def main():
    """
    Función principal que orquesta la obtención y procesamiento de datos asincrónicamente.
    """
    data = await fetch_data()
    result = await process_data()
    print(f"{data}, {result}")

# Ejecutar la función principal en el bucle de eventos asincrónico
asyncio.run(main())
