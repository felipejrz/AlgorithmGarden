# 350. Intersection of Two Arrays II

# Dadas dos matrices enteras nums1 y nums2, devuelva una matriz de su intersección.
# Cada elemento en el resultado debe aparecer tantas veces como se muestra en ambas
# matrices y puede devolver el resultado en cualquier orden.

# Ejemplo 1:

# Entrada: nums1 = [1,2,2,1], nums2 = [2,2]
# Salida: [2,2]
# Ejemplo 2:

# Entrada: nums1 = [4,9,5],
# nums2 = [9,4,9,8,4]
# Salida: [4,9]
# Explicación: [9,4] también se acepta.


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        comunes = []
        # Crear un diccionario para contar las ocurrencias en nums2
        count = {}
        for num in nums2:
            count[num] = count.get(num, 0) + 1

        # Verificar cada número en nums1
        for num in nums1:
            if (
                count.get(num, 0) > 0
            ):  # Si existe en nums2 y hay ocurrencias disponibles
                comunes.append(num)
                count[num] -= 1  # Reducir la cuenta de ocurrencias disponibles

        return comunes
