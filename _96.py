# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution1:
    cache = {}

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n in self.cache.keys():
            return self.cache[n]

        if n == 0:
            return 1

        if n <= 2:
            return n

        res = 0
        for i in range(n):
            res += self.numTrees(i) * self.numTrees(n - i - 1)

        self.cache[n] = res

        return res


class Solution2:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = {0: 1}

        for i in range(1, n + 1):
            res = 0
            for j in range(i):
                res += dp[j] * dp[i - j - 1]

            dp[i] = res

        return dp[n]


if __name__ == '__main__':
    # s = Solution1()
    # print(s.numTrees(3))
    s = Solution2()
    print(s.numTrees(3))
