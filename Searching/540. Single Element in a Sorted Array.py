class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,h = 0,len(nums)-1
        while l < h:
            m = (l+h)//2
            if nums[m] == nums[m ^ 1]:
                l = m + 1
            else:
                h = m
        return nums[l]
