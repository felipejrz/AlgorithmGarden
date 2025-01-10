from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Paso 1: Calcular la frecuencia máxima de cada letra requerida por todas las palabras en words2
        max_freq = {}
        for word in words2:
            word_freq = {}
            for char in word:
                if char in word_freq:
                    word_freq[char] += 1
                else:
                    word_freq[char] = 1
            # Actualizamos la frecuencia máxima de cada letra
            for char, count in word_freq.items():
                if char in max_freq:
                    max_freq[char] = max(max_freq[char], count)
                else:
                    max_freq[char] = count

        # Paso 2: Verificar para cada palabra en words1 si es un conjunto universal
        result = []
        for word in words1:
            word_freq = {}
            for char in word:
                if char in word_freq:
                    word_freq[char] += 1
                else:
                    word_freq[char] = 1

            # Verificar si la palabra tiene las frecuencias suficientes para ser un conjunto universal
            is_universal = True
            for char, count in max_freq.items():
                if word_freq.get(char, 0) < count:
                    is_universal = False
                    break

            if is_universal:
                result.append(word)

        return result
