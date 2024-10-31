import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return x**2 - 6*x + 5

# Intervalos 
a, b = 2, 3
num_subintervalos = 10 
intervalos_no_biseccion = []

# Calcular los puntos de división en el intervalo
puntos = np.linspace(a, b, num_subintervalos + 1)

# Evaluar cada subintervalo
for i in range(len(puntos) - 1):
    x1, x2 = puntos[i], puntos[i+1]
    f_x1, f_x2 = f(x1), f(x2)
    
    # Verificar si los valores en los extremos tienen el mismo signo
    if f_x1 * f_x2 > 0:
        intervalos_no_biseccion.append((x1, x2))

# Graficar la función
x = np.linspace(a - 1, b + 1, 500)  
y = f(x)

plt.plot(x, y, label="f(x) = x^2 - 6x + 5", color="blue")
plt.axhline(0, color="gray", linestyle="--") 

# Resaltar los intervalos donde no se puede aplicar el método de Bisección
for intervalo in intervalos_no_biseccion:
    x1, x2 = intervalo
    plt.fill_betweenx([-10, 10], x1, x2, color="red", alpha=0.3, label="No aplicable" if intervalo == intervalos_no_biseccion[0] else "")

# Ajustes de la gráfica
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Intervalos donde el método de Bisección no es aplicable")
plt.legend()
plt.ylim(-10, 10)  # Limitar el eje y para mejor visualización
plt.grid(True)
plt.show()
