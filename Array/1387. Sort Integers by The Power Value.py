class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        d = {1:0}
        
        def computePower(n):
            if n not in d:
                if n % 2 == 0:
                    d[n] = computePower(n / 2) + 1 
                else:
                    d[n] = computePower(3 * n + 1) + 1
                    
            return d[n]
        
        arr = []
        
        for i in range(lo,hi+1):
            arr.append((computePower(i),i))
        
        return sorted(arr,key = lambda i : i[0])[k-1][1]
