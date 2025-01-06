# Solucion Medio Eficiente
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         arr = []
#         for i in range(n + 1):
#             arr += [bin(i)[2:].count("1")]
#         return arr


# Solucion Mas Eficiente
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Inicializa la lista con ceros
        arr = [0] * (n + 1)
        for i in range(1, n + 1):
            arr[i] = arr[i >> 1] + (
                i & 1
            )  # Usa el desplazamiento y el bit menos significativo
        return arr
