class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        length = len(A)
        
        if length == 1:
            return 0
        
        from itertools import permutations
        cases = (A[0], B[0])
        LS = (A, B)
        res = []
        
        
        for c in cases:
            for L1, L2 in permutations(LS, 2):
                i = 0
                count = 0
                while i < length:
                    if L1[i] == c:
                        pass
                    elif L1[i] != c and L2[i] == c:
                        count += 1
                    else:
                        count = -1
                        break
                
                    i += 1
                
                if count != -1:
                    res.append(count)
        
        if not res:
            return -1
        
        return min(res)