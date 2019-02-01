# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A:
            return 0

        la = len(A)
        i = 0
        res = 0
        while i < la:
            j = i
            while j < la:
                s = sum(A[i:j + 1])
                if s % K == 0:
                    res += 1
                    print(A[i:j + 1])
                j += 1

            i += 1
        return res


class Solution2(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A:
            return 0

        la = len(A)
        i = 0
        res = 0
        while i < la:
            j = i
            s = 0
            while j < la:
                s += A[j]
                if s % K == 0:
                    res += 1
                j += 1

            i += 1
        return res


import collections


class Solution3(object):
    def subarraysDivByK(self, A, K):
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)

        count = collections.Counter(P)
        return int(sum(v * (v - 1) / 2 for v in count.values()))


class Solution4:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        pass

if __name__ == '__main__':
    s = Solution()
    print(s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))

    s = Solution4()
    print(s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
    # print(s.subarraysDivByK([0 for _ in range(1000)], 1000))
