class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        min = float('inf')
        print(min)
        for i in prices:
            if i < min:
                min = i
        
            ganancia  = i - min

            if ganancia > max:
                max = ganancia 
        return max