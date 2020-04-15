class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        R = 1
        ans[0] = 1
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        
        print(ans)
        
        for i in reversed(range(len(nums))):
            ans[i] = ans[i] * R
            R *= nums[i]
        
        print(ans)
        return ans
