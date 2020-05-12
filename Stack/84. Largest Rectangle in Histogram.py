class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        ans = 0
        s = [-1]
        
        for i in range(n):
            while(heights[i] < heights[s[-1]]):
                h = heights[s.pop()]
                w = i-1-s[-1]
                ans = max(ans,h*w)
            s.append(i)
        
        
        return ans
