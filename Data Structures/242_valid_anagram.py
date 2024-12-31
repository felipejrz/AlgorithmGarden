class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Si las longitudes son diferentes, no pueden ser anagramas
        if len(s) != len(t):
            return False

        # Usamos un diccionario para contar las ocurrencias de cada letra en 's'
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Restamos las ocurrencias usando las letras en 't'
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False

        # Si el diccionario está vacío o todas las cuentas son 0, es un anagrama
        return True
