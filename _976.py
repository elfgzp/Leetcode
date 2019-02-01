# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        A = sorted(A, key=lambda v: v)

        i = len(A) - 1
        res = 0
        while i - 2 >= 0:
            m, r, l = A[i], A[i - 1], A[i - 2]

            if m == 0 or r == 0 or l == 0:
                res = 0

            if r + l > m:
                res = m + r + l
                break

            i -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.largestPerimeter([3, 6, 2, 3]))
