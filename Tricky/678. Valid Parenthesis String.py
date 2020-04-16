class Solution:
    def checkValidString(self, s: str) -> bool:
        l = h = 0
        for c in s:
            l += 1 if c=="(" else -1
            h += 1 if c!=")" else -1
            if h<0: break
            l = max(l,0)
        return l == 0
