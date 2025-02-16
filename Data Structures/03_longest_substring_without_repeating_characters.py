#3. Longest Substring Without Repeating Characters

#Dada una cadena s, encuentre la longitud de la más larga Subcadena 
#Sin caracteres duplicados.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        max_len = 0
        start = 0  # Puntero

        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= start:
                # Si el carácter está repetido y está dentro de la subcadena actual
                start = dic[s[i]] + 1  # Ajusta el inicio justo después de la repetición

            dic[s[i]] = i  # Actualiza el índice del carácter
            max_len = max(max_len, i - start + 1)  # Calcula la longitud máxima

        return max_len
