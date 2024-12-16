class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Forma muy ineficiente 
        # aux = {}
        # count = 0
        # while count < len(nums):
        #     value = nums[count]
        #     if value in aux:
        #         # Hacer esto mientras se itera con un for causa problemas 
        #         # Si se hace lo mismo con un while no causa este problema
        #         # De manera normal que es de 0 a n pero si se hace de 
        #         # manera inversa no da errores
        #         # del nums[count]
        #         del nums[count] # Elimina el duplicado
        #     else:
        #         aux[value] = True
        #         count += 1         


        # Esta la opcion mas eficiente 
        # Los set son una estructura de datos 
        # Los elementos de un set son único, lo que significa que no puede haber elementos duplicados.
        # Los set son desordenados, lo que significa que no mantienen el orden de cuando son declarados.
        # s = set([5, 4, 6, 8, 8, 1])
        # print(s) #{1, 4, 5, 6, 8}
        # Sorted ordena ese conjunto de datos pero en LISTA
        # nums[:] remplaza TODOS los valores de la LISTA principal
        nums[:] = sorted(set(nums)) 
        return len(nums)
