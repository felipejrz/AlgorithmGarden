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
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
