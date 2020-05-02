class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        l = len(A)
        return (all(A[i] <= A[i+1] for i in range(l-1)) or all(A[i] >= A[i+1] for i in range(l-1)))
