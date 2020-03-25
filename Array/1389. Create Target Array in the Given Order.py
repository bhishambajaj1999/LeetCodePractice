class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        t = []
        for i,v in zip(index,nums):
            t.insert(i,v)
        return t
