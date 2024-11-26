# Sin poder usar alguna funcion este es el metodo más rapido
# La búsqueda binaria divide el rango por la mitad en cada iteración, 
# haciendo que la solución sea rápida incluso para números grandes.
# Complejidad: 𝑂(log𝑥), mucho más rápida que una iteración lineal 
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right