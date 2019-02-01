# -*- coding: utf-8 -*-
__author__ = 'gzp'


class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        len_nums = len(nums)

        if len_nums <= 1:
            return len_nums

        dp = [1] * len_nums
        cnt = [1] * len_nums
        max_len = 1

        for i in range(len_nums):
            for j in range(i + 1):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]

            max_len = max(max_len, dp[i])

        return sum([cnt[i] for i in range(len_nums) if dp[i] == max_len])


if __name__ == '__main__':
    s = Solution()
    print(s.findNumberOfLIS([1, 3, 5, 4, 7]))
