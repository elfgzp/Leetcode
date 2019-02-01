# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 10:
            return N

        num = [int(n) for n in str(N)[::-1]]
        n = len(num)
        ind = -1

        for i in range(1, n):
            if num[i] > num[i - 1] or (ind != -1 and num[i] == num[ind]):
                ind = i

        if ind == -1:
            return N

        res = '9' * ind + str(num[ind] - 1) + "".join(map(str, num[ind + 1:]))
        return int(res[::-1])
