class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num+1)
        for i in range(num+1):
            if i%2:
                res[i] = res[i-1] + 1
            else:
                res[i] = res[i//2]
        return res
