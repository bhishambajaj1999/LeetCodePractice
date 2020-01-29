from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        k = Counter(nums)
        for i in k:
            if(k[i] >= 2):
                return i
