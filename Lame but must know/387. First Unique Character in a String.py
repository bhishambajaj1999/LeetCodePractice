class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        k = Counter(s)
        k1 = 0
        ind = -1
        
        for i in s:
            if k[i] == 1:
                ind = k1
                break
            k1 += 1
        
        return ind
