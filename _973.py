# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not points or K == 0:
            return []

        res = sorted(points, key=lambda point: point[0] ** 2 + point[1] ** 2)
        return res[:K]


if __name__ == '__main__':
    s = Solution()
    print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
