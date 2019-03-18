class Solution1:
    def bitwiseComplement(self, N: int) -> int:
        N = bin(N)
        N = N[2:]
        _N = ''
        for n in N:
            if n == '0':
                _N += '1'
            else:
                _N += '0'
        
        return int(_N, 2)

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        """
        利用 N + ~N = '0b111...11'
        得出 '0b111...11' - N = ~N
        """
        return int(len(bin(N)[2:]) * '1', 2) - N
