# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # p[i] = min(dp[i], dp[j] + i // j);

        if n <= 1:
            return 0

        dp = {}

        for i in range(3, n + 1):
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    dp[i] = min(dp.get(i, i), dp.get(j, j) + i // j)

        return dp.get(n, n)


if __name__ == '__main__':
    s = Solution()
    print(s.minSteps(6))
