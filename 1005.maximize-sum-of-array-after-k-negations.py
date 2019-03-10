class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        
        if not A:
            return 0
        
        if K == 0:
            return sum(A)
        
        for _ in range(K):
            self._largestSumAfterKNegations(A)
            
        return sum(A)
    
    def _largestSumAfterKNegations(self, A):
        min_index = A.index(min(A))
        A[min_index] = -A[min_index]

