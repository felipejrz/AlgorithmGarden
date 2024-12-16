class Solution:
    def reverseBits(self, n: int) -> int:
        # Convertimo el valor en binario y lo rellenamos a que sean 32 bits
        lis = bin(n)[2:].zfill(32)

        # Le damos la vuelta a valor
        lis = lis[::-1]

        # Lo convertimos a entero se coloca el 2 para que sepa que es de binario a decimal
        reversed_bits = int(lis, 2)
        # print(reversed_bits)
        return reversed_bits
