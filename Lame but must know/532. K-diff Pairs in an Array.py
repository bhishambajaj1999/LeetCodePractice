
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        r = 0
        for i in c:
            if i + k in c and k > 0 or c[i] > 1 and k == 0:
                r += 1
        return r
