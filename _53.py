# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        sum_nums, max_sum = 0, nums[0]

        for num in nums:
            sum_nums = 0 if sum_nums < 0 else sum_nums
            sum_nums += num
            max_sum = max(sum_nums, max_sum)

        return max_sum
