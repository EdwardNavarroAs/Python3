# ¿Qué es la distribución de datos?
# La distribución de datos es una lista de todos los valores posibles y la frecuencia con la que se produce cada valor.

"""
Estas listas son importantes cuando se trabaja con estadísticas y ciencia de datos.

El módulo random de NumPy ofrece métodos que devuelven distribuciones de datos generadas aleatoriamente.

Conceptos importantes:
- Distribución aleatoria:
    Una distribución aleatoria es un conjunto de números aleatorios que siguen una determinada función de densidad de probabilidad.

- Función de densidad de probabilidad: 
    Una función que describe una probabilidad continua, es decir, la probabilidad de todos los valores posibles en un arreglo.
"""

# Visualización de distribuciones con Seaborn
# Seaborn es una biblioteca basada en Matplotlib para trazar gráficos. Se utiliza para visualizar distribuciones aleatorias de datos.

# Histograma y Curva de Densidad
# Un histograma visualiza la frecuencia de los datos, y una curva de densidad muestra cómo se distribuyen de forma continua.
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Datos
data = [0, 1, 2, 1, 1, 5]

# Crear el histograma y la curva de densidad (comentado para activar visualización)
#sns.histplot(data, bins=6, color="blue", alpha=0.6, label="Histograma")  # Histograma
#sns.kdeplot(data, color="red", linewidth=2, label="Curva de Densidad")   # Curva de densidad

# Añadir etiquetas y leyenda
# descomentar para ver el resultado
"""
plt.title("Histograma y Curva de Densidad")
plt.xlabel("Valores")
plt.ylabel("Frecuencia/Densidad")
plt.legend()
plt.show()
"""

"""
Distribución normal
La distribución normal es una de las distribuciones más importantes.

También se la denomina distribución gaussiana en honor al matemático alemán Carl Friedrich Gauss.

Se ajusta a la distribución de probabilidad de muchos eventos, por ejemplo, puntuaciones de CI, latidos del corazón, etc.

La curva de una distribución normal también se conoce como curva de campana debido a su forma de campana.
"""
# Para generar una distribución normal de datos en NumPy se utiliza el método random.normal().
# Tiene tres parámetros:
#   loc - (Media) donde se encuentra el pico de la campana.
#   scale - (Desviación estándar) cómo se distribuyen los datos alrededor de su valor medio.
#   size - La forma del arreglo de datos devuelto.

print("Distribución Normal")
print("La distribución normal es una de las distribuciones más importantes. Se ajusta a la mayoría de eventos en el mundo real.")

print("\nEjemplo 1: Generando una distribución de datos normal de 10 elementos:")
x = np.random.normal(size=10)
print(f"Resultado: \n{x}\n")

print("\nEjemplo 2: Generando una distribución de datos normal de tamaño 2x3:")
x = np.random.normal(size=(2, 3))
print(f"Resultado: \n{x}\n")

print("\nEjemplo 3: Generando una distribución de datos normal de tamaño 2x3, con media 1 y desviación estándar de 2:")
x = np.random.normal(loc=1, scale=2, size=(2, 3))
print(f"Resultado: \n{x}\n")

# Generar y graficar la distribución normal
data = np.random.normal(size=10000)
sns.kdeplot(data, color="red", linewidth=2, label="Curva de Densidad")   # Curva de densidad

plt.title("Distribución de Datos Normal")
plt.xlabel("Valores")
plt.ylabel("Frecuencia/Densidad")
plt.legend()
plt.show()

"""
Distribución Binomial
La distribución binomial es una distribución discreta.

Distribución discreta:
- Una distribución que se define en un conjunto separado de eventos, como el resultado de un lanzamiento de moneda (cara o cruz).
- Por el contrario, una distribución continua se define en un rango infinito de valores, como la altura de las personas (170, 170.1, 170.11, etc.).

Describe el resultado de escenarios binarios, p. ej., al lanzar una moneda, el resultado será cara o cruz.
"""

# Para generar una distribución binomial de datos en NumPy se utiliza el método random.binomial().
# Tiene tres parámetros:
#   n: número de intentos.
#   p: probabilidad de ocurrencia de cada intento (p. ej., para el lanzamiento de una moneda, 0.5 cada uno).
#   size: la forma del arreglo de datos devuelto.

print("Distribución Binomial")
print("La distribución binomial representa eventos discretos, como el resultado de lanzar una moneda, que solo tiene dos posibles resultados: cara o cruz.")

# Ejemplo 1: Generando datos de una distribución binomial
print("\nEjemplo 1: Generando un arreglo de datos obtenidos al lanzar una moneda 10 veces, repetido 10 veces:")
# Generar 10 experimentos, cada uno con 10 intentos y una probabilidad de éxito de 0.5
# La función binomial genera el número de éxitos en cada experimento de 10 intentos
b1 = np.random.binomial(n=10, p=0.5, size=10)
print(f"Resultado: \n{b1}\n")

sns.histplot(b1, kde=False, bins=10, color='blue')

plt.title("Distribución de Datos Binomial")
plt.xlabel("Valores")
plt.ylabel("Frecuencia/Densidad")
plt.show()

# Diferencia entre distribución normal y binomial
# La principal diferencia es que la distribución normal es continua mientras que la binomial es discreta, pero si hay suficientes puntos de datos será bastante similar a la distribución normal con cierta ubicación y escala.
# Generar 1000 muestras de una distribución normal
normal_data = np.random.normal(loc=50, scale=5, size=1000)

# Generar 1000 muestras de una distribución binomial
binomial_data = np.random.binomial(n=100, p=0.5, size=1000)

# Graficar la estimación de densidad para la distribución normal
sns.kdeplot(normal_data, label='Normal', color='blue')

# Graficar la estimación de densidad para la distribución binomial
sns.kdeplot(binomial_data, label='Binomial', color='red')

plt.title("Diferencia entre distribución normal y binomial")
plt.xlabel("Valores")
plt.ylabel("Frecuencia/Densidad")
plt.legend()
plt.show()

"""
Distribución de Poisson
La distribución de Poisson es una distribución discreta que calcula cuántas veces puede ocurrir un evento en un intervalo de tiempo específico. 
Por ejemplo, si en promedio alguien come dos veces al día, ¿cuál es la probabilidad de que coma tres veces en un día?

La distribución de Poisson es comúnmente usada para modelar eventos raros en un intervalo de tiempo o espacio fijo.
"""

# Para generar una distribución de Poisson en NumPy se utiliza el método random.poisson().
# Tiene dos parámetros:
#   lam: tasa o número promedio de ocurrencias (por ejemplo, 2 para el caso anterior).
#   size: la forma del arreglo de datos devuelto.
print("Distribución Poisson")
print("La distribución Poisson representa eventos discretos, calculando cuántas veces puede ocurrir un evento en un intervalo de tiempo o espacio.")

# Ejemplo 1: Generar una distribución aleatoria de tamaño 1x10 para una tasa de ocurrencia de 2
print("\nEjemplo 1: Generar un arreglo de datos con la ocurrencia promedio de 2 en cada intervalo de tiempo, para 10 intervalos:")
p1 = np.random.poisson(lam=2, size=10)
print(f"Resultado: \n{p1}\n")

sns.histplot(p1, kde=False, bins=10, color='blue')

plt.title("Distribución de Datos Poisson")
plt.xlabel("Número de ocurrencias")
plt.ylabel("Frecuencia/Densidad")
plt.show()

"""
Distribución uniforme
Se utiliza para describir la probabilidad en la que cada evento tiene las mismas posibilidades de ocurrir.

Por ejemplo, generación de números aleatorios.
"""

# Para generar una distribución uniforme en NumPy se utiliza el método random.uniform().
# Tiene tres parámetros:
#   low: límite inferior; por defecto, 0.0.
#   high: límite superior; por defecto, 1.0.
#   size: la forma del arreglo de datos devuelto.
print("Distribución Uniforme")
print("La distribución Uniforme se utiliza para describir la probabilidad en la que cada evento tiene las mismas posibilidades de ocurrir.")

# Ejemplo 1: Generar una muestra de distribución uniforme de tamaño 10
print("\nEjemplo 1: Generando una muestra de distribución uniforme de tamaño 10")

u1 = np.random.uniform(size=10)
print(f"Resultado: \n{u1}\n") 

sns.kdeplot(u1, label='Uniforme', color='blue')
plt.title("Distribución de Datos Uniforme")
plt.xlabel("Número de ocurrencias")
plt.ylabel("Frecuencia/Densidad")
plt.show()


"""
Distribución logística

La distribución logística se utiliza para describir el crecimiento.
Se utiliza ampliamente en el aprendizaje automático en regresión logística, redes neuronales, etc.
"""

# Para generar una distribución logistica en NumPy se utiliza el método random.logistics().
# Tiene tres parámetros:
#   loc: media, donde se encuentra el pico. El valor predeterminado es 0.
#   scale: desviación estándar, la uniformidad de la distribución. El valor predeterminado es 1.
#   size: la forma del arrglo de datos devuelto.
print("Distribución Logistica")
print("La distribución logistica se utiliza para describir el posible crecimiento de un fenomeno fisico.")

# Ejemplo 1: # Generar 1000 muestras de una distribución logistica con media 1 y desviacion estandar 2:
print("\nEjemplo 1: Generando 1000 muestras de una distribución logistica con media 1 y desviacion standar 2")
l1 = np.random.logistic(loc=1, scale=2, size=1000)

print(f"Resultado: \n{l1}\n") 

sns.kdeplot(l1, label='logistica', color='blue')
plt.title("Distribución de Datos logistica")
plt.xlabel("Número de ocurrencias")
plt.ylabel("Frecuencia/Densidad")
plt.show()

"""
Distribución exponencial

La distribución exponencial se utiliza para describir el tiempo hasta un próximo evento conocido, por ejemplo, fracaso/éxito, etc.
"""

# Para generar una distribución exponencial en NumPy se utiliza el método random.exponential().

# Tiene dos parámetros:
#   escale: inversa de la tasa; el valor predeterminado es 1,0.
#   size: la forma del arreglo de datos devuelto.
print("Distribución Exponencial")
print("La distribución exponencial se utiliza para describir el tiempo hasta un próximo evento en un proceso de Poisson.")

# Ejemplo 1: # Generar 1000 muestras de una distribución exponencial:
print("\nEjemplo 1: Generando 1000 muestras de una distribución exponencial")
e1 = np.random.exponential(scale=2, size=1000)

print(f"Resultado: \n{e1}\n")  

sns.kdeplot(e1, label='exponencial', color='blue')
plt.title("Distribución de Datos exponencial")
plt.xlabel("Número de ocurrencias")
plt.ylabel("Frecuencia/Densidad")
plt.show()

"""
Distribución de Rayleigh

La distribución de Rayleigh se utiliza en el procesamiento de señales.
"""

# Para generar una distribución rayleigh en NumPy se utiliza el método random.rayleigh().

# Tiene dos parámetros:
#   escale: inversa de la tasa ; el valor predeterminado es 1,0.
#   size: la forma del arreglo de datos devuelto.

print("Distribución rayleigh")
print("La distribución de Rayleigh se utiliza en el procesamiento de señales.")

# Ejemplo 1: # Generar 1000 muestras de una distribución rayleigh:
print("\nEjemplo 1: Generando 1000 muestras de una distribución rayleigh")
r1 = np.random.rayleigh(size=1000)

print(f"Resultado: \n{r1}\n")  # Corrige p1 a u1

sns.kdeplot(r1, label='rayleigh', color='blue')
plt.title("Distribución de Datos rayleigh")
plt.xlabel("Número de ocurrencias")
plt.ylabel("Frecuencia/Densidad")
plt.show()

# otras distribuciones
"""
Distribución Chi-cuadrado

Se utiliza en estadísticas para evaluar la relación entre dos variables categóricas o en pruebas de hipótesis.
Ejemplo: Comparar la varianza de una muestra con una varianza teórica.
"""
# Distribución Chi-cuadrado
print("Distribución Chi-cuadrado")
print("La distribución Chi-cuadrado se utiliza en pruebas estadísticas como la prueba de bondad de ajuste o la independencia.")

chi_data = np.random.chisquare(df=2, size=1000)  # df: grados de libertad

sns.kdeplot(chi_data, label='Chi-cuadrado', color='purple')
plt.title("Distribución Chi-cuadrado")
plt.xlabel("Valores")
plt.ylabel("Frecuencia/Densidad")
plt.legend()
plt.show()

"""
Distribucion Gamma

Modela la duración hasta que ocurran k eventos en un proceso de Poisson.
Ejemplo: Modelar la cantidad de lluvia acumulada en un día.
"""
# Distribución Gamma
print("Distribución Gamma")
print("La distribución Gamma se utiliza para modelar la duración hasta que ocurran k eventos en un proceso de Poisson.")

gamma_data = np.random.gamma(shape=2, scale=2, size=1000)  # shape=k, scale=theta

sns.kdeplot(gamma_data, label='Gamma', color='orange')
plt.title("Distribución Gamma")
plt.xlabel("Valores")
plt.ylabel("Frecuencia/Densidad")
plt.legend()
plt.show()

"""
Distribución beta

Se utiliza para modelar probabilidades o proporciones.
Ejemplo: Tasa de éxito en ensayos clínicos.
"""
# Distribución Beta
print("Distribución Beta")
print("La distribución Beta se utiliza para modelar probabilidades o proporciones.")

beta_data = np.random.beta(a=2, b=5, size=1000)  # a y b son parámetros de forma

sns.kdeplot(beta_data, label='Beta', color='cyan')
plt.title("Distribución Beta")
plt.xlabel("Valores")
plt.ylabel("Frecuencia/Densidad")
plt.legend()
plt.show()
