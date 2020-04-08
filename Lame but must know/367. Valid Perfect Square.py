class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while(num):
            num -= i
            i += 2
            if(num<0): return False
        return True
