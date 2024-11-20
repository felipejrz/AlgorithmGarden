class Solution:
    def __init__(self):
        self.roman = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000, 
        'IV': 4,  # 4 = 5 - 1
        'IX': 9,  # 9 = 10 - 1
        'XL': 40, # 40 = 50 - 10
        'XC': 90, # 90 = 100 - 10
        'CD': 400, # 400 = 500 - 100
        'CM': 900  # 900 = 1000 - 100
    }


    def romanToInt(self, s: str) -> int:
        total = 0
        value2 = 0
        for count, value in enumerate(s):
            if count < len(s) - 1:
                next_value = s[count + 1]
                value2 = value + next_value
                # print(value2)
            if value2 in self.roman:
                total += self.roman[value2]
                print(self.roman[value2])
            elif value in self.roman:
                total += self.roman[value]
                print(self.roman[value])
        return total
