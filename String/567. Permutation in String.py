class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        sl,pl = len(s),len(p)
        
        if sl < pl:
            return False

        
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
                return True
            
        return False
