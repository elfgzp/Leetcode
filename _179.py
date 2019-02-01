# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        str_nums = list(map(str, nums))
        len_nums = len(nums)

        for i in range(len_nums):
            for j in range(1, len_nums - i):
                if str_nums[j] + str_nums[j - 1] > str_nums[j - 1] + str_nums[j]:
                    str_nums[j],  str_nums[j - 1] = str_nums[j - 1],  str_nums[j]

        val = ''.join(str_nums)
        if val[0] == '0':
            return '0'

        return val