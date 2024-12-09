class Solution:
    def addBinary(self, a: str, b: str) -> str:
         # Interpreta como base 2 y lo convierte a entero
         # Por lo tanto en ves de convertilo en 
         # Entero 1 o 11 lo convierte en 1 y 3 
        return(bin(int(a, 2) + int(b, 2))[2:])
        