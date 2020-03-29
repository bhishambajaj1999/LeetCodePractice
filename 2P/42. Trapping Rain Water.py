class Solution:
    def trap(self, height: List[int]) -> int:
        a = ml = mr = l = 0
        r = len(height) - 1
        
        while l<r:
            if(height[l] < height[r]):
                if(height[l] > ml):
                    ml = height[l]
                else:
                    a += ml - height[l]
                l += 1
            else:
                if(height[r] > mr):
                    mr = height[r]
                else:
                    a += mr - height[r]
                r -= 1
        
        return a
                
