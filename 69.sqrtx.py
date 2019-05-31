class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        n = x
        xn = n // 2
        while xn**2 - n >= 1:
            xn = xn - (xn**2 - n) / (2 * xn)

        return int(xn)
