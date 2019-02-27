#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (35.43%)
# Total Accepted:    20.8K
# Total Submissions: 58.4K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
# 案例:
#
#
# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.
#
#
#
#
# 注意事项：您可以假定该字符串只包含小写字母。
#
#


class Solution:
    def firstUniqChar(self, s: str) -> int:
        str_set = sorted(list(set(s)), key=lambda x: s.index(x))
        for char in str_set:
            if s.count(char) == 1:
                return s.index(char)
        return -1
