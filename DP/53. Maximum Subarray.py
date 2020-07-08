class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        
        p = [0] * l
        n = [0] * l
        
        p[0],n[0] = nums[0],nums[0]
        for i in range(1,l):
            a = nums[i]
            v = (a,p[i-1] + a,n[i-1] + a)
            p[i] = max(v)
            n[i] = min(v)
        
        return max(p)
    
# Kadane
    
    def maxSubArray1(self, nums: List[int]) -> int:
        
        m, msf = nums[0],nums[0]
        
        for i in range(1,len(nums)):
            m = max(nums[i],nums[i] + m)
            msf = max(m,msf)
        
        return msf
