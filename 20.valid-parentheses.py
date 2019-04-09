#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (36.40%)
# Total Accepted:    62K
# Total Submissions: 166.3K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#


class Solution:

    def isValid(self, s: str) -> bool:
        m = {')': '(', ']': '[', '}': '{'}
        stack = []
        i = 0
        while i < len(s):
            if s[i] in [')', ']', '}']:
                if not stack:
                    return False
            
                if stack[-1] != m[s[i]]:
                    return False
                else:
                    stack.pop(-1)
            else:
                stack.append(s[i])
            
            i += 1
        
        if stack:
            return False
        
        return True
            