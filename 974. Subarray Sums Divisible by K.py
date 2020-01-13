class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        #Initializing
        s,r = 0,0
        d={}
        d[0] = 1
        
        
        for i in A:
            #Ongoing sum 
            s += i
            
            if(((s-K)%K) in d):
                r += d[(s-K) % K]
            
            #Creating Hashmap 
            if((s-K)%K in d):
                d[(s-K)%K] += 1
            
            else:
                d[(s-K)%K] = 1
        
        return r
