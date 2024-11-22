class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Contador para el número de elementos que no son `val`
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Mueve el elemento a la posición correcta
                k += 1
        return k 
        