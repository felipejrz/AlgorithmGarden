# 415. Add Strings

# Dados dos enteros no negativos, num1 y num2 representados como cadena, devuelva la suma de num1 y num2 como una cadena.

# Debe resolver el problema sin usar ninguna biblioteca incorporada para manejar enteros grandes
# (como BigInteger). Tampoco debe convertir las entradas en enteros directamente.

# Ejemplo 1:
# Entrada: num1 = "11", num2 = "123"
# Salida: "134"

# Ejemplo 2:
# Entrada: num1 = "456", num2 = "77"
# Salida: "533"

# Ejemplo 3:
# Entrada: num1 = "0", num2 = "0"
# Salida: "0"

# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         sys.set_int_max_str_digits(10000)
#         return str(int(num1)+int(num2))


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialize pointers for num1 and num2
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        # Loop through both strings from end to start
        while i >= 0 or j >= 0 or carry:
            digit1 = ord(num1[i]) - ord("0") if i >= 0 else 0
            digit2 = ord(num2[j]) - ord("0") if j >= 0 else 0

            # Calculate the sum of digits and carry
            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(str(total % 10))

            # Move to the next digits
            i -= 1
            j -= 1

        # Since we've added digits from least significant to most, reverse the result
        return "".join(result[::-1])
