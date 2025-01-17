from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        
        # Función para construir el arreglo original dado el primer valor
        def canConstruct(first_val: int) -> bool:
            original = [first_val]
            
            # Construir el resto del arreglo original usando derived
            for i in range(n - 1):
                original.append(original[-1] ^ derived[i])
            
            # Verificar la consistencia en el último paso
            return (original[-1] ^ derived[-1]) == original[0]
        
        # Probar ambos casos posibles para original[0]
        return canConstruct(0) or canConstruct(1)
