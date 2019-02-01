# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        res = False
        pre_sum = 0
        dic = {0: 0}

        if 0 == k:
            for i in range(1, len(nums)):
                if 0 == nums[i] and nums[i - 1] == nums[i]:
                    return True
        else:
            for j, n in enumerate(nums):
                pre_sum += n

                mod = pre_sum % k

                if mod in dic and j - dic[mod] > 0:
                    res = True
                    break

                dic[mod] = j

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.checkSubarraySum([0, 0], 0))
