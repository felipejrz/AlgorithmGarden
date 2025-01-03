class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        max_palindrome = ""
        for i in range(len(s)):
            # Palíndromo con longitud impar
            odd_palindrome = expand_around_center(i, i)
            # Palíndromo con longitud par
            even_palindrome = expand_around_center(i, i + 1)
            # Escoge el más largo
            max_palindrome = max(
                max_palindrome, odd_palindrome, even_palindrome, key=len
            )

        return max_palindrome
