class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [],[]
        

    def addNum(self, num: int) -> None:
        s,l = self.heaps
        heappush(s,-heappushpop(l,num))
        if(len(l) < len(s)):
            heappush(l,-heappop(s))


    def findMedian(self) -> float:
        s,l = self.heaps
        if (len(l) > len(s)):
            return float(l[0])
        
        return (l[0] - s[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
