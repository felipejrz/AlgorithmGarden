# Solucion Ineficiente
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n == 1:
#             return True

#         for i in range(1, 50):
#             # print(n, 2**i)
#             if n == 2**i:
#                 return True

#             if n < 2**i:
#                 break
#         return False

# Esta es la solucion mas eficiente

# Un número es potencia de 2 si en su representación binaria solo tiene un bit establecido en 1.
# n&(n−1) borra el bit menos significativo, y será igual a 0 solo si n es una potencia de 2.
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and (n & (n - 1)) == 0


# Solucion que si entiendo y eficiente
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Checar si es mayor a 0
        if n <= 0:
            return False
        # Mientras sea divisible entre 2 hacer el bucle
        while n % 2 == 0:
            n //= 2
        # Si es 1 regresamos True
        return n == 1
