class Solution:
    def maxScoreSightseeingPair1(self, A: List[int]) -> int:
        """
        max(A[i] + A[j] + i - j) = max(A[i] + i) + max(A[j] - j)
        i < j
        """
        
        sell, buy = 0, float('-inf')
        for i, val in enumerate(A):
            sell = max(sell, val - i + buy)
            buy = max(buy, val + i)
        return sell
    
    def maxScoreSightseeingPair(self, A: List[int]) -> int:        
        cur = res = 0
        for a in A:
            res = max(res, cur + a)
            cur = max(cur, a) - 1
        return res
