class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target) 
        
        except: 
            return bisect.bisect_left(nums, target)
            
