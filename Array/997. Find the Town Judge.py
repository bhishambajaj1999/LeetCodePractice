# Total Influx - Total Efflux == N - 1

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust == []:
            return 1
        
        t = [0] * (N+1)
        for i in trust:
            t[i[0]] -= 1
            t[i[1]] += 1
        
        for i in range(N+1):
            if t[i] == N-1:
                return i
    
        return -1
