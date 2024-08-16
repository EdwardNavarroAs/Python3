# Tema 5: iteradores en Python

# Un iterador es un objeto que contiene una cantidad contable de valores.

# Un iterador es un objeto que se puede iterar, lo que significa que se pueden recorrer todos los valores.

# Técnicamente, en Python, un iterador es un objeto que implementa el protocolo de iterador, que consta de los métodos __iter__() y __next__().


# ----------------------------------------------------------------------------------------------------------------------------------------
# Objetos Iterables
# Las listas, tuplas, diccionarios y conjuntos son objetos iterables. Son contenedores iterables de los que se puede obtener un iterador.
# Todos estos objetos tienen un método iter() que se utiliza para obtener un iterador:
print("\nOBJETOS ITERABLES EN PYTHON\n")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)


print("Las listas, tuplas, diccionarios y conjuntos son objetos iterables de los que se puede obtener un iterador")
print(f"ejemplo de objeto iterable -> objeto: {mytuple}, tipo: {type(mytuple)}")
print(f"iterador del objeto {type(mytuple)}: iterador: {myit}, tipo: {type(myit)} ")
print('')

# Incluso las cadenas de texto son objetos iterables y pueden devolver un iterador
my_string = "hola desde python"
print("Las cadenas de texto tambien son objetos iterables")
print(f"iterador de la cadena de texto '{my_string}': iterador {my_string}, tipo: {type(my_string)}")

print("\nITERANDO SOBRE OBJETOS ITERABLES\n")
# En python es posible utilizar un bucle for para iterar sobre un objeto iterable: