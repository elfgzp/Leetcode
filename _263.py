# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False

        while num % 2 == 0:
            num = num / 2

        while num % 3 == 0:
            num = num / 3

        while num % 5 == 0:
            num = num / 5

        return num == 1

