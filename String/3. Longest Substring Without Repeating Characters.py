class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = ""
        m = 0
        for i in s:
            if i in d:     
                m=max(m,len(d))   
                d = d[d.index(i) + 1:]
            d += i


        return max(m,len(d))

