class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        
        n1, n2 = 0, 1
        
        i = 1
        while i < N:
            n1, n2 = n2, n1 + n2
            i += 1
        
        return n2

