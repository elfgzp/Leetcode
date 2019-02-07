# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        total = 0
        per = 0

        flowerbed = [1, 0] + flowerbed + [0, 1]

        for each in flowerbed:
            if each == 0:
                per += 1
            else:
                per = 0

            if per >= 3:
                total += 1
                per = 1

        return total >= n