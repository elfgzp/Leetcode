class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        
        avg = s // 3
        cnt = 0
        s = 0
        
        for i in A:
            s += i
            if s == avg:
                cnt += 1
                s = 0
        
        return cnt == 3
