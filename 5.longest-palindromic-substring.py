#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (24.51%)
# Total Accepted:    39.8K
# Total Submissions: 161.5K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
#
#


class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)

        dp = [[False for _ in range(len_s)] for _ in range(len_s)]

        end = 0
        start = 0

        for j in range(len_s):
            for i in range(0, j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        if j - i + 1 >= end - start + 1:
                            start, end = i, j
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i + 1 >= end - start + 1:
                            start, end = i, j

        return s[start: end + 1]




