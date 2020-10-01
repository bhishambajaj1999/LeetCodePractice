class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([1 for i in range(32) if (n >> i & 1)]) #bitwise shift operator