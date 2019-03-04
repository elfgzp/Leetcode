class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        
        from collections import Counter
        
        i = 1
        counter = Counter(A[0])
        res = []
        
        
        while i < len(A):
            counter &= Counter(A[i])
            i += 1
        
        if not counter or not counter.elements():
            return res
        
        for k, v in counter.items():
            res += [k for _ in range(v)]
            
        return res