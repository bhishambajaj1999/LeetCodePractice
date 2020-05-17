# Sliding window

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sl,pl = len(s),len(p)
        if sl < pl:
            return []
        
        res = []
        
        pc = Counter(p)
        sc = Counter()
        
        for i in range(sl):
            sc[s[i]] += 1
            
            if i >= pl:
                if sc[s[i-pl]] == 1:
                    del sc[s[i-pl]]
                else:
                    sc[s[i-pl]] -= 1
                
            if pc == sc:
                res.append(i - pl + 1)
            
        return res
