class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2  # Encuentra el punto medio
            
            if nums[mid] == target:
                return mid  # Si el valor es encontrado, devuelve el índice
            elif nums[mid] < target:
                left = mid + 1  # Si el valor es mayor, busca a la derecha
            else:
                right = mid - 1  # Si el valor es menor, busca a la izquierda
        
        # Si no se encuentra el valor, devuelve el índice donde debería insertarse
        return left
        