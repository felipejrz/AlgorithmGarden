class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        # Ordenamos las palabras por longitud de mayor a menor
        words.sort(key=len, reverse=True)
        # print(words)

        # Usamos un set para almacenar las palabras ya vistas
        seen = set()

        for word in words:
            # Si la palabra ya ha sido vista como subcadena de otra
            for longer_word in seen:
                if word in longer_word:
                    result.append(word)
                    break
            # Añadimos la palabra a seen después de procesarla
            seen.add(word)

        return result
