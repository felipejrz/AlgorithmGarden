# Dado un número de matriz enteros, devuelva el tercer número máximo distinto en esta matriz.
# Si el tercer máximo no existe, devuelva el número máximo.

# Ejemplo 1:

# Entrada: Nums = [3,2,1]
# Salida: 1
# Explicación:
# El primer máximo distinto es 3.
# El segundo máximo distinto es 2.
# El tercer máximo distinto es 1.
# Ejemplo 2:

# Entrada: Nums = [1,2]
# Salida: 2
# Explicación:
# El primer máximo distinto es 2.
# El segundo máximo distinto es 1.
# El tercer máximo distinto no existe, por lo que el máximo (2) se devuelve en su lugar.
# Ejemplo 3:

# Entrada: Nums = [2,2,3,1]
# Salida: 1
# Explicación:
# El primer máximo distinto es 3.
# El segundo máximo distinto es 2 (ambos 2 se cuentan juntos ya que tienen el mismo valor).
# El tercer máximo distinto es 1.


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))  # Eliminamos duplicados
        nums.sort(reverse=True)  # Ordenamos de mayor a menor

        return (
            nums[2] if len(nums) >= 3 else nums[0]
        )  # Si hay al menos 3 elementos, tomamos el tercero, si no, el máximo
