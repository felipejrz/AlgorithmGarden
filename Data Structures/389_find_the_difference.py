# 389. Find the Difference
# Te dan dos cuerdas s y t.

# La cadena T se genera mediante cadenas de barras aleatorias y luego agregue una letra más en una posición aleatoria.

# Devuelve la carta que se agregó a t.

# Ejemplo 1:

# Entrada: S = "ABCD", T = "ABCDE"
# Salida: "E"
# Explicación: 'E' es la carta que se agregó.
# Ejemplo 2:

# Entrada: s = "", t = "y"
# Salida: "Y"


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        resultado = 0

        # Hacemos XOR entre todos los caracteres de s y t
        for char in s + t:
            resultado ^= ord(
                char
            )  # Convertimos cada carácter a su valor ASCII y aplicamos XOR

        # Convertimos el resultado de vuelta a un carácter
        return chr(resultado)
