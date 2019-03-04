#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#
# https://leetcode-cn.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (51.75%)
# Total Accepted:    8.7K
# Total Submissions: 16.7K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# 给定一个二进制数组， 计算其中最大连续1的个数。
#
# 示例 1:
#
#
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
#
#
# 注意：
#
#
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。
#
#
#


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        i = 0

        for n in nums:
            if n:
                i += 1
                res = max(i, res)
            else:
                i = 0

        return res


