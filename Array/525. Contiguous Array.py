class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        d = {0:0}
        c = 0
        ml =0
        
        for i,num in enumerate(nums,1):
            if num == 0:
                c -= 1
            else:
                c += 1
        
            if c in d:
                ml = max(ml,i - d[c])
            else:
                d[c] = i
        
        return ml
