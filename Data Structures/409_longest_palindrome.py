# 409. Longest Palindrome

# Dada una cadena s que consiste en letras minúsculas o mayúsculas, devuelva la longitud de la más larga
# palíndromo que se pueden construir con esas letras.

# Las letras son sensibles a los casos, por ejemplo, "Aa" no se considera un palíndromo.

# Ejemplo 1:

# Entrada: S = "abccccdd"
# Salida: 7
# Explicación: Un palíndromo más largo que se puede construir es "dccaccd", cuya longitud es 7.
# Ejemplo 2:

# Entrada: S = "a"
# Salida: 1
# Explicación: El palíndromo más largo que se puede construir es "A", cuya longitud es 1.
from itertools import permutations


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}  # Diccionario para contar la frecuencia de cada letra
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        length = 0
        has_odd = (
            False  # Para verificar si hay al menos un carácter con frecuencia impar
        )

        for count in freq.values():
            if count % 2 == 0:
                length += count  # Si es par, lo usamos completamente
            else:
                length += count - 1  # Usamos la parte par
                has_odd = True  # Marcamos que hay un impar

        return (
            length + 1 if has_odd else length
        )  # Si hay impares, añadimos 1 para el centro
