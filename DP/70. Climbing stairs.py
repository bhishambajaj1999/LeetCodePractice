class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        fib = [0 for _ in range(n + 1)]
        fib[0] = 1
        fib[1] = 1
        fib[2] = 2
        for i in range(3, n+1):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[-1]