#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0, 1]
        if num < 2:
            return dp[:num + 1]

        k = 1

        for i in range(2, num + 1):
            if i >= k * 2:
                k *= 2

            if i == k:
                dp.append(1)
            else:
                dp.append(dp[k] + dp[i - k])

        return dp


