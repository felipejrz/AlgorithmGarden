class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # Ajuste para que sea 0-indexado
            remainder = columnNumber % 26  # Encuentra el resto
            result = (
                chr(remainder + ord("A")) + result
            )  # Convierte el resto en una letra
            columnNumber //= 26  # Reduce el número dividiendo por 26

        return result
