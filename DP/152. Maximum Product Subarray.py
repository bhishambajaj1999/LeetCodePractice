class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        p = [0] * l
        n = [0] * l
        p[0],n[0] = nums[0],nums[0]
        for i in range(1,len(nums)):
            a = nums[i]
            v = (a,p[i-1]*a,n[i-1]*a)
            p[i] = max(v)
            n[i] = min(v)
        
        print(p)
        print(n)
        return max(p)
