# Bézout's theorem
# 2 Jugs, unlimited supply of water, find if particular volume can be achieved

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if(x+y < z):
            return False
        if(x==z or y==z or x+y==z or z==0):
            return True
        return z % math.gcd(x,y) == 0
