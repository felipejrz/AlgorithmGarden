# 387. First Unique Character in a String
# Dada una cadena S, encuentre el primer carácter no repetitivo en él y devuelva su índice. Si no existe, return -1.

# Ejemplo 1:

# Entrada: S = "Leetcode"

# Salida: 0

# Explicación:

# El personaje 'L' en el índice 0 es el primer carácter que no ocurre en ningún otro índice.

# Ejemplo 2:

# Entrada: S = "LoveleetCode"

# Salida: 2

# Ejemplo 3:
# Entrada: S = "AABB"

# Salida: -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        conteo = {}
        arr = list(s)

        for char in s:
            conteo[char] = conteo.get(char, 0) + 1

        for i, char in enumerate(s):
            if conteo[char] == 1:
                return i

        return -1
