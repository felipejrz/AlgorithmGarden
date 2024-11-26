class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        # Variables para almacenar los resultados previos
        prev1, prev2 = 1, 1
        
        # Calculamos dp(n) iterativamente
        for i in range(2, n + 1):
            current = prev1 + prev2  # Suma de los dos anteriores
            prev2 = prev1  # Actualizamos prev2
            prev1 = current  # Actualizamos prev1
        
        return prev1