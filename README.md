# cafe
# Incluimos un código en python de un problema visto en clase "enfiramiento de un objeto usando el método de euler"
# Tenemos un café a 90° que se enfría en una habitación a temperatura ambiente de 25°
# nuestro modelo es:
dT / dt = -k *(T - Tamb)
donde:
- T (t) es la temperatura del café en el tiempo.
-  Tamb = 25°
-  k = 0.5 esta es la constante de enfriamiento
-  Condición inicial: T(0) = 90°
# Implementamos el método de euler con paso h = 0.1 en el intervalo t [0,2]
# El código calcula la aproximación numérica y la compara con la solución analítica
T(t) = Tamb + (T0 - Tamb) e^-kt
# Cuando corremos el código generamos una gráfica que nos muestra: 
- La curva exacta de la solución analítica
- Los puntos aproximados que obtuvimos con eulr
- 
