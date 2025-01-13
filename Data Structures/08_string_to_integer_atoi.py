class Solution:
    def myAtoi(self, s: str) -> int:
        # Limites del entero con signo de 32 bits
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1

        # 1. Eliminar espacios iniciales
        s = s.lstrip()
        if not s:
            return 0

        # 2. Determinar el signo
        signo = 1
        if s[0] == "-":
            signo = -1
            s = s[1:]  # Quitar el signo del inicio
        elif s[0] == "+":
            s = s[1:]  # Quitar el signo del inicio

        print(s)
        # 3. Leer los dígitos hasta encontrar un carácter no numérico
        resultado = 0
        for char in s:
            if char.isdigit():
                resultado = resultado * 10 + int(char)
            else:
                break  # Detenerse al encontrar un carácter no numérico

        # 4. Aplicar el signo
        resultado *= signo

        # 5. Ajustar el resultado al rango de 32 bits
        if resultado < INT_MIN:
            return INT_MIN
        if resultado > INT_MAX:
            return INT_MAX

        return resultado
