class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newnums = sorted(nums1 + nums2)

        # Si el número de elementos es impar, devuelve el elemento central
        if len(newnums) % 2 == 1:
            return float(newnums[len(newnums) // 2])
        else:  # Si el número de elementos es par, calcula el promedio de los dos centrales
            return (newnums[len(newnums) // 2 - 1] + newnums[len(newnums) // 2]) / 2
