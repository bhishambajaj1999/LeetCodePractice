class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        
        for i in range(1,n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]
        
        return dp[n]
    
    # Catalan Number 
    # (2n)! / (n! * (n+1)!)
    """
    def numTrees(self, n: int) -> int:
        return math.factorial(2*n) // (math.factorial(n) * math.factorial(n+1))
    """
    
