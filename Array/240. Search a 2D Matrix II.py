class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            i,j,l = len(matrix)-1,0,len(matrix[0])
            while(i>=0 and j<l):
                if(matrix[i][j] == target): return True
                elif(matrix[i][j] > target): i -= 1
                else: j += 1
            
        return False
