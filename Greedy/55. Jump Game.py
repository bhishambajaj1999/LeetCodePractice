class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        i = 0
        mi = nums[i]
        while i < len(nums) and i <= mi:
            ni = nums[i] + i
            mi = max(mi,ni)
            i += 1
        if i==len(nums):
            return True
        return False
