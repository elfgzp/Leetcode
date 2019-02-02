# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1]

        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]
