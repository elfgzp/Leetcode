#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#
# https://leetcode-cn.com/problems/power-of-three/description/
#
# algorithms
# Easy (42.20%)
# Total Accepted:    15K
# Total Submissions: 34.9K
# Testcase Example:  '27'
#
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
# 
# 示例 1:
# 
# 输入: 27
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: 0
# 输出: false
# 
# 示例 3:
# 
# 输入: 9
# 输出: true
# 
# 示例 4:
# 
# 输入: 45
# 输出: false
# 
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
# 
#


class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            n = n / 3

        return n == 1


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        import math
        tem = math.log10(n) / math.log10(3)
        return tem == int(tem)