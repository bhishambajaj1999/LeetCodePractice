class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            len1 = self.cp(s,i,i)
            len2 = self.cp(s,i,i+1)
            lenf = max(len1,len2)
            if (lenf > end - start):
                start = i - (lenf - 1) // 2
                end = i + lenf//2
        
        return s[start:end+1]
    
    def cp(self, s,left,right):
        if not s or left > right : 
            return 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return right - left - 1
        
