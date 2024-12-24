class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Diccionario para mapear caracteres de 's' a 't'
        dic = {}

        # Si las longitudes no coinciden, no pueden ser isomorfos
        if len(s) != len(t):
            return False

        # Iterar sobre cada carácter de las cadenas
        for i in range(len(s)):
            # Si el carácter de 's' no está en el diccionario
            if s[i] not in dic:
                # Verificar que el carácter de 't' no haya sido asignado a otro carácter
                if t[i] in dic.values():
                    return False
                # Asignar la relación s[i] -> t[i] en el diccionario
                dic[s[i]] = t[i]
            else:
                # Si el carácter ya está mapeado, verificar que coincida con el carácter actual de 't'
                if dic[s[i]] != t[i]:
                    return False

        # Si pasamos todas las verificaciones, las cadenas son isomorfas
        return True
