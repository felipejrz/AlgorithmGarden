class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Índice para insertar el próximo número no cero
        insert_pos = 0

        # Mover todos los números diferentes de cero al frente
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        # Rellenar el resto con ceros
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
