class Solution:
    def divisorGame(self, N: int) -> bool:
        
        
        res = False
        
        while N > 1:
            x = 1
            while x < N:
                if N % x == 0:
                    res = not res
                    break
                x += 1
            else:
                res = not res
            N -= x
        
        return res
