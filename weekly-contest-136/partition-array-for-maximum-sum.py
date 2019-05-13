class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        length = len(A)
        dp = [0] * (length + 1)
        for i in range(length):
            m = float('-inf')
            j = i - 1
            while j >= -1 and i - j <= K:
                m = max(m, A[j + 1])
                dp[i + 1] = max(dp[j + 1] + (i - j) * m, dp[i + 1])
                j -= 1
        return dp[length]
