class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        p,s = 0,0
        k = collections.Counter(arr)
        k = {keys:value for keys,value in sorted(k.items(),key = lambda item:item[1],reverse = True)}
        l = len(arr) / 2
        for i in k:
            if(s < l):
                s += k[i]
                p += 1
            else:
                break
        return p
