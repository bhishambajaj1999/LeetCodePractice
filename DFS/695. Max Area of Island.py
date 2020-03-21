class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        a=[]
        s=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                a.append(self.area(s,grid,i,j))
        
        return max(a)
    
    def area(self,s,grid,r,c):
        if(r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c] != 1 or (r,c) in s):
            return 0
        s.add((r,c))
        return (1 + self.area(s,grid,r+1,c) + self.area(s,grid,r-1,c) + self.area(s,grid,r,c+1) + self.area(s,grid,r,c-1))
