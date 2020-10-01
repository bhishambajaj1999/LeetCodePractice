class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        i = 0
        count = 0
        while i < len(s)-1:
            if roman[s[i]] >= roman[s[i+1]]:
                count += roman[s[i]]
                i += 1
            else:
                count += roman[s[i+1]] - roman[s[i]]
                i += 2
        if i<len(s):
            count += roman[s[i]]
        
        return count
            
            