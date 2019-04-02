class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return '0'
        
        res = []
        while N != 0:
            quotient, remainder = N // -2, N % -2
            N = quotient
            if remainder < 0:
                remainder += 2
                N += 1
            
            res.append(str(remainder))
        
        return ''.join(res[::-1])
