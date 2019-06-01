class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if dividend ^ divisor >= 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            minus, quotient = divisor, 1
            while dividend > (minus << 1):
                minus <<= 1
                quotient <<= 1
            dividend -= minus
            ans += quotient
            
        ans *= sign
        
        if ans < -2**31 or ans > 2**31 - 1:
            return 2**31 - 1
        
        return ans

