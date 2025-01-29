# 383. Ransom Note

# Dadas dos cadenas ransomnote y revista, devuelva verdadero si Ransomnote se
# puede construir usando las letras de la revista y falso de lo contrario.

# Cada letra en la revista solo se puede usar una vez en Ransomnote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Contamos la frecuencia de cada carácter en ambas cadenas
        count1 = Counter(ransomNote)
        count2 = Counter(magazine)
        print(count2)

        # Verificamos si para cada carácter en ransomNote, magazine tiene al menos la misma cantidad
        for char in count1:
            if count1[char] > count2.get(
                char, 0
            ):  # Si magazine no tiene suficientes caracteres
                return False
        return True
