class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1

        signo = -1 if x < 0 else 1
        n = abs(x)

        invertido = 0

        while n > 0:
            ultimo_digito = n % 10
            invertido = invertido * 10 + ultimo_digito
            n //= 10

        if invertido < INT_MIN or invertido > INT_MAX:
            return 0

        return signo * invertido
