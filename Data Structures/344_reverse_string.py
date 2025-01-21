# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         s = "".join(s)
#         s = list(s[::-1])
#         print(s)
#         return s

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1  # Inicializa punteros
        
        while left < right:
            # Intercambia elementos
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
