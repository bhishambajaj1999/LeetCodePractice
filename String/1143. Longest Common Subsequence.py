class Solution:
    def longestCommonSubsequence(self, X: str, Y: str) -> int:
        '''
        # Recursion - Exponential time = 2^n, Exceeded, Top Down
        def lcs(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            elif text1[i] == text2[j]:
                return 1 + lcs(i+1,j+1)
            else:
                return max(lcs(i+1,j),lcs(i,j+1))
        
        return lcs(0,0)
        '''
        
        # DP - Bottom up, Time = mn
        
        m = len(X) 
        n = len(Y) 

        L = [[None]*(n+1) for i in range(m+1)] 


        for i in range(m+1): 
            for j in range(n+1): 
                if i == 0 or j == 0 : 
                    L[i][j] = 0
                elif X[i-1] == Y[j-1]: 
                    L[i][j] = L[i-1][j-1]+1
                else: 
                    L[i][j] = max(L[i-1][j] , L[i][j-1]) 


        return L[m][n] 
