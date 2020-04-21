# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        size = binaryMatrix.dimensions()
        r,c = 0,size[1]-1
        res = -1
        if(size[0] == 0 or size[1] == 1):
            return -1
        while( r<size[0] and c>=0 ):
            if(binaryMatrix.get(r,c) == 1):
                res = c
                c -= 1
            else:
                r += 1
        return res
