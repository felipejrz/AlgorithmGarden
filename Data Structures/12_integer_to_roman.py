# class Solution:
#     def intToRoman(self, num: int) -> str:
#         roman = {
#             1000: 'M',
#             900: 'CM',
#             500: 'D',
#             400: 'CD',
#             100: 'C',
#             90: 'XC',
#             50: 'L',
#             40: 'XL',
#             10: 'X',
#             9: 'IX',
#             5: 'V',
#             4: 'IV',
#             1: 'I'
#         }

#         result = ""

#         for i, symbol in roman.items():
#             while num >= i:
#                 result += symbol
#                 print(num)
#                 num -= i


#         return result
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        result = []

        for i, roman in roman:
            # 3   = 3749// 1000
            count = num // i  # Calcular cuántas veces cabe el valor en el número

            if count:  # Si count > 0, agregar el símbolo correspondiente
                result += [roman * count]
            num %= i  # Actualizar el número restante

            if num == 0:
                break

        return "".join(result)
