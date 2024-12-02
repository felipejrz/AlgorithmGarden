from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # Aplicamos XOR a cada elemento
        return result

# Ejemplo
# # print(result, num)
#           0       4
#           4       1
#           5       2
#           7       1
#           6       2
#           4       