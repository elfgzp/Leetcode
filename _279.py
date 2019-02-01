# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 0:
            return 0

        min_num = None

        max_square_root = 1
        while max_square_root * max_square_root <= n:
            max_square_root += 1
        else:
            max_square_root -= 1

        start_square_root = max_square_root
        while start_square_root >= 1:
            residue = n
            square_root = start_square_root

            num_squares = []
            while True:
                square = square_root ** 2
                if residue - square < 0:
                    square_root -= 1
                else:
                    residue -= square
                    num_squares.append(square)
                    if residue == 0:
                        break

            len_num_squares = len(num_squares)
            if min_num is None:
                min_num = len_num_squares
            elif len_num_squares < min_num:
                min_num = len_num_squares

            start_square_root -= 1

        return min_num


class Solution2:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = list()
        q.append([n, 0])
        visited = [False for _ in range(n + 1)]
        visited[n] = True

        while any(q):
            num, step = q.pop(0)
            i = 1
            tNum = num - i ** 2
            while tNum >= 0:
                print(i ** 2)
                if tNum == 0:
                    return step + 1

                if not visited[tNum]:
                    q.append((tNum, step + 1))
                    visited[tNum] = True

                i += 1
                tNum = num - i ** 2
            print('\n')


class Solution3:
    _dp = [0]

    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += list((min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,))
        return dp[n]


import math


class Solution4(object):
    cache = {}

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.cache:
            return self.cache[n]

        upper = int(math.sqrt(n))
        for i in range(upper, 0, -1):
            # 找到了
            if n == i * i:
                self.cache[n] = 1
                return 1
            else:
                ret = self.numSquares(n - i * i)
                if ret:
                    if n in self.cache:
                        self.cache[n] = min(ret + 1, self.cache[n])
                    else:
                        self.cache[n] = ret + 1

        if n in self.cache:
            return self.cache[n]
        return None


import collections


class Solution5(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = collections.defaultdict(int)
        y = 1
        while y * y <= n:
            dp[y * y] = 1
            y += 1
        for x in range(1, n + 1):
            y = 1
            while x + y * y <= n:
                if x + y * y not in dp or dp[x] + 1 < dp[x + y * y]:
                    dp[x + y * y] = dp[x] + 1
                y += 1
        return dp[n]


class Solution6(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 用上限n初始化结果数组
        nums = [i for i in range(n + 1)]
        # 从1开始填充结果数组
        for i in range(1, n + 1):
            j = 1
            # 所有可能包含的平方数j
            while j * j <= i:
                nums[i] = min(nums[i], nums[i - j * j] + 1)
                j += 1
        return nums[n]


if __name__ == '__main__':
    s = Solution()
    # # print(s.numSquares(12))
    # # print(s.numSquares(13))
    # print(s.numSquares(43))
    # print('----')

    # s2 = Solution2()
    # print(s2.numSquares(43))

    # s3 = Solution3()
    # print(s3.numSquares(43))
    #
    # s4 = Solution4()
    # print(s4.numSquares(43))
    #
    # s5 = Solution5()
    # print(s5.numSquares(43))

    s6 = Solution6()
    print(s6.numSquares(43))
