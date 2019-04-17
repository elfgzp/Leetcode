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
        dp = [[0 for _ in range(len_s)] for _ in range(len_s)]
        
        l, r = 0, 0
        
        for i in range(len_s):
            for j in range(i + 1):
                dis = i - j
                if dis <= 2:
                    if s[i] == s[j]:
                        dp[j][i] = 1
                        if dis > r - l:
                            l, r = j, i
                elif s[i] == s[j] and dp[j + 1][i - 1]:
                    dp[j][i] = 1
                    if dis > r - l:
                        l, r = j, i
                        
        return s[l: r + 1]
                    