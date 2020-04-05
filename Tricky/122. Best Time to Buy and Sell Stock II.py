class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t = 0
        for i in range(1,len(prices)):
            if(prices[i] > prices[i-1]):
                t += prices[i] - prices[i-1]
        return t
