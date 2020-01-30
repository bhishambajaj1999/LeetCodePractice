class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if (n == 0): 
            return 0
        f,g = [0] * n,[0] * n
        g[0] = -prices[0]
        for i in range(1,n):
            f[i] = max(f[i - 1], g[i - 1] + prices[i])
            if (i >= 2): g[i] = max(g[i - 1], f[i - 2] - prices[i])
            else: g[i] = max(g[i - 1], -prices[i])
        return f[n - 1]
