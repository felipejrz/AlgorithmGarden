class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        row = []
        for i in range(numRows):
            if i == 0:
                row += [1]
                # Con el += no me deja agregar directamente listas a listas
                triangle.append(row)
            else:
                for j in range(i + 1):
                    if  j == 0 or j == i:
                        row += [1]
                    elif i + 1 >= 3:
                        row += [triangle[i - 1][j] + triangle[i - 1][j - 1]]
                triangle.append(row)
            row = []
        return triangle

###ESTE ES UNO MAS EFICIENTE Y MENOS LARTO ABRA QUE ESTUDIAR MAS
# class Solution:
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         # Inicializar una lista vacía para almacenar el triángulo
#         triangle = []

#         # Crear cada fila del triángulo de Pascal
#         for i in range(numRows):
#             # Cada fila comienza con un 1
#             row = [1] * (i + 1)  # Crea una lista con 'i+1' elementos, todos 1

#             # Calcular los valores intermedios de la fila
#             for j in range(1, i):
#                 # Los valores intermedios son la suma de los dos elementos directamente arriba
#                 row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

#             # Añadir la fila completa al triángulo
#             triangle.append(row)

#         return triangle
