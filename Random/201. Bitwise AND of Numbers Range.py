class Solution:
    def rangeBitwiseAnd(self, a: int, b: int) -> int:
        if a == b:
            return a
        while a < b:
            b -= (b & -b)
        return b
