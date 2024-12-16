# Solucion  muy ineficiente
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         conteo = {} # Diccionario para contar cuantos
#         max = 0
#         count = 0
#         for num in nums:
#             if num in conteo:
#                 conteo[num] += 1
#             else:
#                 conteo[num] = 1

#         # Si ponemos solo i me imprime un arreglo
#         # Ejemplo (3: 2), (2: 1)
#         for i, j in conteo.items():
#             if j > count:
#                 count = j
#                 max = i
#         return max


# Solucion super eficiente mucho mas pequeña que las demas
# [2,2,1,1,1,2,2]
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Se ordena el arreglo
        nums.sort()
        # [1,1,1,2,2,2,2]
        # Devolvemos el elemento en la posición media
        # El operador // es una divicion con piso
        return nums[len(nums) // 2]
