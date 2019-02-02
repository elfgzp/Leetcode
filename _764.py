class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = {0: cost[0], 1: cost[1]}
        len_cost = len(cost)

        for i in range(2, len_cost):
            dp[i] = min(dp[i - 2] + cost[i], dp[i - 1] + cost[i])

        return min(dp[len_cost - 1], dp[len_cost - 2])
