class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        O(1)
        """
        p = 0
        for i in range(len(nums)):
            el = nums[i]
            if(el != 0):
                nums[p],nums[i] = nums[i],nums[p]
                p += 1
