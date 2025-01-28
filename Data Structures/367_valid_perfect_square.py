# 367. Valid Perfect Square

# Dado un número de intergro positivo, regrese verdadero si NUM es un cuadrado perfecto o falso de otra manera.
# To Perfect Square es un entero que es el cuadrado de un entero. En otras palabras, es el producto de SubGeger consigo mismo.
# No debe usar ninguna función de biblioteca incorporada, como SQRT.

# Ejemplo 1:

# Entrada: num = 16
# Salida: Verdadero
# Explicación: devolvemos verdadero porque 4 * 4 = 16 y 4 es un entero.

# Ejemplo 2:

# Entrada: num = 14
# Salida: Falso
# Explicación: Devuelve falso porque 3.742 * 3,742 = 14 y 3,742 no es un entero.


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        tolerancia = 1e-10

        #  Método de aproximación de Newton (también conocido como método de Newton-Raphson)
        estimacion = num / 2.0

        # Iteramos hasta que la diferencia sea menor que la tolerancia
        while True:
            nueva_estimacion = 0.5 * (estimacion + num / estimacion)
            if abs(nueva_estimacion - estimacion) < tolerancia:
                return nueva_estimacion % 1 == 0
            estimacion = nueva_estimacion
