#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#


class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length <= 1:
            return True

        dp = [0] * (length)
        dp[0] = nums[0]

        for i in range(1, length):
            if dp[i - 1] - 1 >= 0:
                dp[i] = max(dp[i - 1] - 1, nums[i])
            else:
                dp[i] = -1

        if dp[-1] >= 0:
            return True

        return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length <= 1:
            return True

        max_step = nums[0]

        for i in range(1, length):
            if max_step - 1 >= 0:
                max_step = max(max_step - 1, nums[i])
            else:
                max_step = -1

        if max_step >= 0:
            return True

        return False
