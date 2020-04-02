class Solution:
    def findLucky(self, arr: List[int]) -> int:
        p = collections.Counter(arr)
        t = -1
        pp = []
        for i in p:
            if(p[i] == i):
                t += 1
                pp.append(i)
                
        return max(pp) if t!=-1 else t
        
