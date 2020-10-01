import numpy as np
class Solution:

    def __init__(self, nums: List[int]):
        self.change=nums
        self.orig=nums
        self.length = len(nums)
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.orig
        
        
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        arr = np.array(self.change)
        np.random.shuffle(arr)
        return arr
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()