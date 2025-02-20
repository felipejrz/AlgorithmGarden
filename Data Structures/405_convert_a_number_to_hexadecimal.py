# 405. Convert a Number to Hexadecimal

# Dada un número entero de 32 bits, devuelva una cadena que represente su representación hexadecimal.
# Para enteros negativos, se utiliza el método de complemento de dos.

# Todas las letras en la cadena de respuestas deben ser caracteres en minúsculas, y no debe haber
# ceros principales en la respuesta, excepto el cero mismo.

# Nota: No puede usar ningún método de biblioteca incorporado para resolver directamente este problema.

# Ejemplo 1:

# Entrada: Num = 26
# Salida: "1a"
# Ejemplo 2:


# Entrada: num = -1
# Salida: "ffffffff" "
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        # num & 0xFFFFFFFF fuerza a que el número se maneje en 32 bits.
        return hex(num & 0xFFFFFFFF)[2:]
