class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = []
        # Lista de caracteres a eliminar 
        caracteres_a_eliminar = [" ", ",", ":", ".", "@", "_", "-", "$", "#", "'", "\\", "{", "}", "\"", "[", "]", "¡", "!", "?", ";", "(", ")", "`"]
        # Se pone en minusculas
        s = s.lower()
        # For para ir eliminando todos los caracteres que sobran
        for char in caracteres_a_eliminar:
            s = s.replace(char, "")
        # Se invierte la cadena para comparar con la original
        s2 = s[::-1]
        # Si si son iguales regresa True
        return s2 == s
        