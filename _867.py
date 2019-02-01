# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        if not A:
            return A

        len_A_0 = len(A[0])

        A_ = [[] for _ in range(len_A_0)]

        for i in range(len_A_0):
            for j in range(len(A)):
                A_[i].append(A[j][i])

        return A_

class Solution2:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        return [
            [A[j][i] for j in range(len(A))]
            for i in range(len(A[0]))
        ]

if __name__ == '__main__':
    s = Solution()
    print(s.transpose([[1,2,3],[4,5,6]]))
