class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Checar si es mayor a 0
        if n <= 0:
            return False
        # Mientras sea divisible entre 3 hacer el bucle
        while n % 3 == 0:
            n //= 3
        # Si es 1 regresamos True
        return n == 1
