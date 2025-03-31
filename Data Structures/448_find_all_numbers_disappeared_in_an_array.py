# 448. Find All Numbers Disappeared in an Array

# Dada una matriz numeros de n enteros donde los números [i] están en el
# rango [1, n], devuelve una matriz de todos los enteros en el rango [1, n] que no aparecen en NUMS.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        se = set(nums)
        final = []
        for i in range(1, len(nums) + 1):
            if i not in se:
                final += [i]
        return final