import numpy as np
import matplotlib.pyplot as plt
import time

# Definir las funciones
def f1(x):
    return x

def f2(x):
    return np.abs(x - 1) + 2

def f3(x):
    return x**2

def f4(x):
    return x**3

def f5(x):
    return x**4

def f6(x):
    return np.where(x > 0, np.log(x), np.nan)

def f7(x):
    return np.where(x >= 0, 2**x, np.nan)

def factorial(x):
    resultado = 1  # Asignar un valor inicial a resultado
    if x == 0 or x == 1:
        resultado = 1
    elif x > 1:
        resultado = x * factorial(x-1)
    return resultado

def f8(x):
    return [factorial(xi) for xi in x]

# Crear un rango de valores para x en el rango de -100 a 100
x_values = np.arange(-100, 101, dtype=float)

# Calcular los valores de y correspondientes para cada función en el nuevo rango de x
y1 = f1(x_values)
y2 = f2(x_values)
y3 = f3(x_values)
y4 = f4(x_values)
y5 = f5(x_values)
y6 = f6(x_values)
y7 = f7(x_values)
y8 = f8(x_values)

# Iniciar la lista para almacenar los tiempos de ejecución
execution_times = []

# Medir el tiempo de ejecución para cada función
for func, y in zip([f1, f2, f3, f4, f5, f6, f7, f8], [y1, y2, y3, y4, y5, y6, y7, y8]):
    start_time = time.time()
    y_values = func(x_values)  # Calcular los valores de y para la función actual
    elapsed_time = time.time() - start_time
    execution_times.append(elapsed_time)

# Graficar las funciones con el nuevo rango de x
plt.figure(figsize=(10, 12))

plt.subplot(4, 2, 1)
plt.plot(x_values, y1)
plt.title('f(x) = x')
plt.xlim(-100, 100)  # Establecer límites del eje x

plt.subplot(4, 2, 2)
plt.plot(x_values, y2)
plt.title('f(x) = |x - 1| + 2')
plt.xlim(-100, 100)  # Establecer límites del eje x

plt.subplot(4, 2, 3)
plt.plot(x_values, y3)
plt.title('f(x) = x^2')
plt.xlim(-100, 100)  # Establecer límites del eje x

plt.subplot(4, 2, 4)
plt.plot(x_values, y4)
plt.title('f(x) = x^3')
plt.xlim(-100, 100)  # Establecer límites del eje x

plt.subplot(4, 2, 5)
plt.plot(x_values, y5)
plt.title('f(x) = x^4')
plt.xlim(-100, 100)  # Establecer límites del eje x

plt.subplot(4, 2, 6)
plt.plot(x_values, y6)
plt.title('f(x) = log(x)')
plt.xlim(-100, 100)  # Establecer límites del eje x

plt.subplot(4, 2, 7)
plt.plot(x_values, y7)
plt.title('f(x) = 2^x')
plt.xlim(-100, 100)  # Establecer límites del eje x

plt.subplot(4, 2, 8)
plt.plot(x_values, y8)
plt.title('f(x) = x!')
plt.xlim(-100, 100)  # Establecer límites del eje x

plt.tight_layout()

# Guardar la gráfica en funciones.jpg
plt.savefig("funciones.jpg")

plt.show()

# Imprimir los tiempos de ejecución
print("Tiempos de ejecución de las funciones:")
for i, func in enumerate([f1, f2, f3, f4, f5, f6, f7, f8]):
    print(f"{func.__name__}: {execution_times[i]} segundos")
