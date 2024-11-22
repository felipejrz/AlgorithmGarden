class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tam = 0
        palabra = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                tam += 1
                palabra = True
            elif palabra:
                return tam
        return tam
