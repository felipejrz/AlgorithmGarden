class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Find regresa la posicion en la que se encuentra la prinera coecidencia 
        # Si no lo encuentra regresa -1
        return haystack.find(needle)