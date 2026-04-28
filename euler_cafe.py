import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
k = 0.5
T_amb = 25
T0 = 90
h = 0.1
t0, tf = 0, 2
N = int((tf - t0) / h)

# Definición de la función diferencial
def f(t, T):
    return -k * (T - T_amb)

# Método de Euler
t_values = [t0]
T_values = [T0]

t = t0
T = T0
for i in range(N):
    T = T + h * f(t, T)
    t = t + h
    t_values.append(t)
    T_values.append(T)

# Solución exacta (para comparar)
t_exact = np.linspace(t0, tf, 100)
T_exact = T_amb + (T0 - T_amb) * np.exp(-k * t_exact)

# Gráfica
plt.plot(t_values, T_values, 'o-', label='Euler (h=0.1)')
plt.plot(t_exact, T_exact, '-', label='Solución exacta')
plt.xlabel('Tiempo t')
plt.ylabel('Temperatura T')
plt.title('Enfriamiento de un café: Euler vs Exacta')
plt.legend()
plt.grid(True)
plt.show()
