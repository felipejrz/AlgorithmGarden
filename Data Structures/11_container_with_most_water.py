class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1  # Inicializar los dos punteros
        max_area = 0

        while left < right:
            # Calculamos el área actual
            width = right - left
            current_area = min(height[left], height[right]) * width

            # Actualizamos el área máxima
            max_area = max(max_area, current_area)

            # Movemos el puntero que apunta a la línea más baja
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
