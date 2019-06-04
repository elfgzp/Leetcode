class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not obstacleGrid:
            return 0

        m = len(obstacleGrid[0])
        n = len(obstacleGrid)

        if m == 1:
            for i in range(n):
                if obstacleGrid[i][0] == 1:
                    return 0
            else:
                return 1

        if n == 1:
            for i in range(m):
                if obstacleGrid[0][i] == 1:
                    return 0
            else:
                return 1

        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        for i in range(1, m):
            dp[0][i] = 1 if obstacleGrid[0][i] != 1 and dp[0][i - 1] != 0 else 0

        for i in range(1, n):
            dp[i][0] = 1 if obstacleGrid[i][0] != 1 and dp[i - 1][0] != 0 else 0

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0

        return dp[-1][-1]
