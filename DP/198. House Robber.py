class Solution:
    def rob(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        elif len(arr) == 1:
            return arr[0]
        elif len(arr) == 2:
            return max(arr)
        
        dp = [None] * len(arr)
        
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
            
        for i in range(2, len(arr)):
            dp[i] = max(dp[i-2] + arr[i], dp[i-1])
            
        return dp[-1]
