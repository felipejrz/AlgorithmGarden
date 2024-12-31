class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = [int(digit) for digit in str(num)]
            num = sum(num)
        return num
