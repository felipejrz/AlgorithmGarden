# El Hamming Weight, también conocido como población de bits o peso de Hamming,
# se refiere a la cantidad de bits 1 que están presentes en la representación
# binaria de un número. Es un concepto importante en teoría de la información y
# criptografía, y se utiliza para medir cuán "lleno" está un número de bits.
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Combierto n en binario
        n = bin(n)[2:]
        # Regreso cuantos 1 tiene el numero
        return n.count("1")
