class Solution:
    # Solucion O(S) temporal, complejidad temporarl O(1) 
    # Más eficiente, sencillo, y sin estructuras auxiliares.
    def longestCommonPrefix(self, strs):
        # Verificamos si haya cadena
        if not strs:
            return ""
        # Tomamos la primer palabra
        prefix = strs[0]

        # El fragmento strs[1:] en Python sirve para crear una sublista de la lista 
        # strs que contiene todos los elementos excepto el primero.
        # Por lo tanto recorre la cadena menos el primero que ese se encuentra en prefix
        for string in strs[1:]:
            print(string[:len(prefix)])
            while string[:len(prefix)] != prefix:
                # Quitar el último carácter
                prefix = prefix[:-1]  
                # Si no queda prefijo, terminamos
                if not prefix:
                    return "" 
        return prefix
