#Sieve

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        P_num = [0, 0] + [1] * (n-2)
        i = 2
        while i**2 < n:
            if P_num[i]:
                P_num[i**2: n: i] = [0] * len(P_num[i**2: n: i])
            i += 1
        return sum(P_num)

