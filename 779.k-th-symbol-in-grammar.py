class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        
        if N == 2:
            return 0 if K == 1 else 1
        
        half = 2**(N - 2)
        if K <= half:
            return self.kthGrammar(N - 1, K)
        else:
            return 1 - self.kthGrammar(N - 1, K - half)

