# 392. Is Subsequence

# Dadas dos cadenas S y T, devuelva verdadero si s es una subsecuencia de t, o falsa de otra manera.

# Una subsecuencia de una cadena es una nueva cadena que se forma a partir de la cadena original
# eliminando algunos (no puede ser ninguno) de los caracteres sin perturbar las posiciones relativas
# de los caracteres restantes. (es decir, "Ace" es una subsecuencia de "abcde" mientras que "AEC" no lo es).

# Ejemplo 1:

# Entrada: S = "ABC", T = "AHBGDC"
# Salida: Verdadero
# Ejemplo 2:

# Entrada: s = "axc", t = "ahbgdc"
# Salida: Falso


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = 0
        b = 0
        while a < len(t) and b < len(s):
            if t[a] == s[b]:
                b += 1
            a += 1

        return b == len(s)
