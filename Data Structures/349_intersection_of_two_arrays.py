# 349. Intersection of Two Arrays

# Dadas dos matrices de números enteros nums1 y nums2, devuelve una matriz de su
# intersección. Cada elemento del resultado debe ser único y puedes devolver el resultado en cualquier orden.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

# Problem
# Forma Ineficiente
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         comunes = []
#         for num in nums1:
#             if num in nums2 and num not in comunes:
#                 comunes.append(num)
#         return comunes


# Forma Eficiente
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convertimos las listas a conjuntos para aprovechar la intersección
        set1 = set(nums1)
        set2 = set(nums2)

        # Calculamos la intersección y la convertimos a lista
        comunes = list(set1 & set2)
        return comunes
