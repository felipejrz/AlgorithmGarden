class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        going_down = False  # Indica si estamos bajando o subiendo

        # Construir las filas del zigzag
        for char in s:
            rows[current_row] += char
            # Cambiar dirección si estamos en la primera o última fila
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Avanzar hacia arriba o hacia abajo
            current_row += 1 if going_down else -1

        # Combinar todas las filas en una sola cadena
        return "".join(rows)
