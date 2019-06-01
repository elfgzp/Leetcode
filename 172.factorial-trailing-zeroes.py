class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        
        n = n // 5
        return n + self.trailingZeroes(n)
  
