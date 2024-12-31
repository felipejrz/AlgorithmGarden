# Solucion ineficiente ya que el in hace que sea muy tardado
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         for i in range(1, len(nums) + 1):
#             if i  not in nums:
#                 return i
#         return 0


# Solucion eficiente
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        suma_esperada = n * (n + 1) // 2
        suma_real = sum(nums)
        return suma_esperada - suma_real
