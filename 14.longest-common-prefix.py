#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.59%)
# Total Accepted:    55.7K
# Total Submissions: 173.1K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        min_str = min(strs, key=lambda x: len(x))
        
        i = 0
        same = ''
        while i < len(min_str):
            not_matched = False
            for s in strs:
                if s[i] != min_str[i]:
                    not_matched = True
                    break
                if not_matched:
                    break

            if not_matched:
                break
            
            same += min_str[i]
                
            i += 1
        
        return same


