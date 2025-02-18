#1. Two Sum

#Dada una matriz de números enteros nums y un destino entero, devuelve 
#los índices de los dos números de modo que se sumen al destino.

#Puede suponer que cada entrada tendría exactamente una solución, 
#y no puede usar el mismo elemento dos veces.

#Puede devolver la respuesta en cualquier orden.

#Ejemplo 1:

#Entrada: nums = [2,7,11,15], target = 9
#Salida: [0,1]
#Explicación: Debido a que nums[0] + nums[1] == 9, devolvemos [0, 1].
#Ejemplo 2:

#Entrada: nums = [3,2,4], target = 6
#Producción: [1,2]
#Ejemplo 3:

#Entrada: nums = [3,3], target = 6
#Salida: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for count, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], count]

            seen[num] = count
