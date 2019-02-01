# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """

        if ops:
            return min(ops, key=lambda x: x[0])[0] * min(ops, key=lambda y: y[1])[1]

        return m * n


if __name__ == '__main__':
    s = Solution()
    print(s.maxCount(
        3,
        3,
        [[2, 1], [1, 2]]
    ))
