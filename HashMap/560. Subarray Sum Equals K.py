class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        r , s = 0 , 0
        d[0] = 1
        for i in nums:
            s += i
            
            if((s-k) in d):
                r += d[s-k]
            
            if(s in d):
                d[s] += 1
            else:
                d[s] = 1

        return r
