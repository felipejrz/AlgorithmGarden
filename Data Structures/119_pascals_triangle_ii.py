class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Inicializar una lista vacía para almacenar el triángulo
        triangle = []

        # Crear cada fila del triángulo de Pascal
        for i in range(rowIndex + 1):
            # Cada fila comienza con un 1
            row = [1] * (i + 1)  # Crea una lista con 'i+1' elementos, todos 1

            # Calcular los valores intermedios de la fila
            for j in range(1, i):
                # Los valores intermedios son la suma de los dos elementos directamente arriba
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            # Añadir la fila completa al triángulo
            triangle.append(row)
        return triangle[rowIndex]