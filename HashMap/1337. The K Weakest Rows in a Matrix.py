class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        s = dict()
        for i in range(len(mat)):
            s[i]= sum(mat[i])
            
        si = sorted(s.values())
        kk = []
        for i in si:
            for j in s:
                if(s[j] == i):
                    kk.append(j)
                    s[j] = float('inf')
            
        return kk[0:k]
