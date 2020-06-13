class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0: return []
        s = [[i] for i in nums]
        nums.sort()
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(s[i]) < len(s[j]) + 1:
                    s[i] = s[j] + [nums[i]]
        
        return max(s, key = len)
