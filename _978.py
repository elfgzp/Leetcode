# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        len_a = len(A)
        dp = {0: 1}

        i = 1
        last_cmp = None
        while i < len_a:
            if A[i - 1] < A[i] and last_cmp != '<':
                dp[i] = dp.get(i - 1, 0) + 1
                last_cmp = '<'
            elif A[i - 1] > A[i] and last_cmp != '>':
                dp[i] = dp.get(i - 1, 0) + 1
                last_cmp = '>'
            elif A[i - 1] == A[i]:
                dp[i] = 1
            else:
                dp[i] = 2

            i += 1
        return max(dp.values())
