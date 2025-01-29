# 374. Guess Number Higher or Lower

# Estamos jugando el juego de Guess. El juego es el siguiente:

# Elijo un número de 1 a n. Tienes que adivinar qué número elegí.

# Cada vez que adivine mal, le diré si el número que elegí es más alto o más bajo que su suposición.

# Llamas a una API int-definido predefinida intunción (int num), que devuelve tres resultados posibles:

# -1: Su suposición es más alta que el número que elegí (es decir, num> elige).
# 1: Tu suposición es más bajo que el número que elegí (es decir, num <pick).
# 0: Tu suposición es igual al número que elegí (es decir, num == elige).
# Devuelve el número que elegí.


class Solution:
    def guessNumber(self, n: int) -> int:
        izq, der = 1, n  # Rango inicial

        while izq <= der:
            mid = (izq + der) // 2  # Calculamos el punto medio
            res = guess(mid)  # Llamamos a la función guess()

            if res == 0:  # Si encontramos el número
                return mid
            elif res == -1:  # Si mid es muy alto, ajustamos el límite superior
                der = mid - 1
            else:  # Si mid es muy bajo, ajustamos el límite inferior
                izq = mid + 1

        return -1
