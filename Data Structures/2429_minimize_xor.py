class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Paso 1: Contar los bits en 1 en num2
        num2_bits = bin(num2).count(
            "1"
        )  # Número de bits en 1 que debe tener el resultado

        # Paso 2: Inicializar el resultado y procesar los bits de num1
        result = 0

        # Copiar los bits en 1 de num1 al resultado, de mayor a menor peso
        for i in range(
            31, -1, -1
        ):  # Recorrer los bits desde el 31 (más significativo) al 0
            if num2_bits == 0:  # Si ya tenemos suficientes bits en 1
                break
            if num1 & (1 << i):  # Si el bit i está en 1 en num1
                result |= 1 << i  # Poner el bit i en 1 en el resultado
                num2_bits -= 1  # Restar un bit requerido

        # Paso 3: Agregar más bits en 1 si es necesario
        for i in range(32):  # Recorrer los bits desde el 0 (menos significativo) al 31
            if num2_bits == 0:  # Si ya hemos puesto suficientes bits en 1
                break
            if not (result & (1 << i)):  # Si el bit i está en 0 en el resultado
                result |= 1 << i  # Poner el bit i en 1 en el resultado
                num2_bits -= 1  # Restar un bit requerido

        # Paso 4: Devolver el resultado
        return result
