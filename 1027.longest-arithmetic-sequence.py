class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        from collections import defaultdict
        length = len(A)
        if length == 2:
            return 2

        m = 2
        dp = defaultdict(dict)
        for j in range(length):
            for i in range(j + 1, length):
                d = A[i] - A[j]
                if j in dp[d]:
                    dp[d][i] = dp[d][j] + 1
                else:
                    dp[d][i] = 2
                m = max(dp[d][i], m)
        return m

